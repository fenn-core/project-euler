#!/usr/bin/env python3
"""
Project Euler README updater with a tiny terminal UI.

Design:
- README text outside EULER_DASHBOARD markers is preserved.
- Problem metadata is read from data/euler_state.json.
- Language implementation flags are edited manually in the TUI.
- Main grid status is checked if a problem is implemented in at least one language.
- Language columns are config-driven and expandable.

Run:
    python tools/euler_readme_tui.py

Suggested repo layout:
    project-euler/
    ├── README.md
    ├── data/
    │   └── euler_state.json
    └── tools/
        └── euler_readme_tui.py
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
STATE_PATH = ROOT / "tools" / "state_seed.json"

START = "<!-- EULER_DASHBOARD_START -->"
END = "<!-- EULER_DASHBOARD_END -->"

BAR_WIDTH = 30

# Add future languages here. The key is stored in JSON.
LANGUAGES = {
    "py": "Python",
    "c": "C",
    "cpp": "C++",
}


@dataclass
class Problem:
    number: int
    title: str
    level: str
    percent: str
    euler_solved: bool
    langs: dict[str, bool]

    @property
    def implemented(self) -> bool:
        return any(self.langs.get(lang, False) for lang in LANGUAGES)


def progress_bar(done: int, total: int, width: int = BAR_WIDTH) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def checkbox(value: bool) -> str:
    return "[x]" if value else "[ ]"


def status(value: bool) -> str:
    return "✅" if value else "⬜"


def ensure_state_exists() -> None:
    if STATE_PATH.exists():
        return

    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    problems = []
    for n in range(1, 1000):
        problems.append(
            {
                "number": n,
                "title": "",
                "level": "L??",
                "percent": "?%",
                "euler_solved": False,
                "langs": {lang: False for lang in LANGUAGES},
            }
        )

    save_state(
        [
            Problem(
                number=p["number"],
                title=p["title"],
                level=p["level"],
                percent=p["percent"],
                euler_solved=p["euler_solved"],
                langs=p["langs"],
            )
            for p in problems
        ]
    )


def load_state() -> list[Problem]:
    ensure_state_exists()
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    problems = []
    for item in data["problems"]:
        langs = {
            lang: bool(item.get("langs", {}).get(lang, False)) for lang in LANGUAGES
        }
        problems.append(
            Problem(
                number=int(item["number"]),
                title=str(item.get("title", "")),
                level=str(item.get("level", "L??")),
                percent=str(item.get("percent", "?%")),
                euler_solved=bool(item.get("euler_solved", False)),
                langs=langs,
            )
        )
    return problems


def save_state(problems: list[Problem]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "languages": LANGUAGES,
        "problems": [
            {
                "number": p.number,
                "title": p.title,
                "level": p.level,
                "percent": p.percent,
                "euler_solved": p.euler_solved,
                "langs": p.langs,
            }
            for p in problems
        ],
    }
    STATE_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def render_dashboard(problems: list[Problem]) -> str:
    total = len(problems)
    euler_solved = sum(p.euler_solved for p in problems)
    implemented = sum(p.implemented for p in problems)

    lines: list[str] = []

    lines.append(START)
    lines.append("")
    lines.append("## Progress")
    lines.append("")
    lines.append(f"**Project Euler solved:** `{euler_solved} / {total}`  ")
    lines.append(f"**Project Euler completion:** `{euler_solved / total * 100:.1f}%`  ")
    lines.append(f"**Project Euler progress:** `{progress_bar(euler_solved, total)}`")
    lines.append("")
    lines.append(f"**Repository implemented:** `{implemented} / {total}`  ")
    lines.append(f"**Repository completion:** `{implemented / total * 100:.1f}%`  ")
    lines.append(f"**Repository progress:** `{progress_bar(implemented, total)}`")
    lines.append("")
    lines.append("## Language Implementation Counts")
    lines.append("")
    lines.append("| Language | Implemented |")
    lines.append("|---|---:|")
    for lang, label in LANGUAGES.items():
        count = sum(p.langs.get(lang, False) for p in problems)
        lines.append(f"| {label} | {count} |")
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("| Symbol | Meaning |")
    lines.append("|---|---|")
    lines.append("| ✅ | Implemented in at least one configured repo language |")
    lines.append("| ⬜ | Not implemented in the repo yet |")
    lines.append("| `[x]` | Implemented in this language |")
    lines.append("| `[ ]` | Not implemented in this language |")
    lines.append("| `Lxx` | Project Euler difficulty level |")
    lines.append("| `%` | Difficulty percentage shown by Project Euler |")
    lines.append("")
    lines.append("## Progress by 100-Problem Block")
    lines.append("")
    lines.append("| Range | Implemented | Progress |")
    lines.append("|---:|---:|---|")
    for start in range(1, 1000, 100):
        end = min(start + 99, 999)
        block = [p for p in problems if start <= p.number <= end]
        done = sum(p.implemented for p in block)
        label = f"{start:03d}–{end:03d}"
        lines.append(
            f"| {label} | {done}/{len(block)} | `{progress_bar(done, len(block), 20)}` |"
        )
    lines.append("")
    lines.append("## Main Grid")
    lines.append("")
    lines.append("Each cell is formatted as: `status problem difficulty`.")
    lines.append("")
    lines.append(
        "`✅` means the problem is implemented in at least one configured repository language."
    )
    lines.append("")
    lines.append("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    for row_start in range(1, 1000, 10):
        cells = []
        for n in range(row_start, min(row_start + 10, 1000)):
            p = problems[n - 1]
            cells.append(
                f"{status(p.implemented)} "
                f"[{p.number:03d}](https://projecteuler.net/problem={p.number}) "
                f"`{p.level}` `{p.percent}`"
            )
        if len(cells) < 10:
            cells.extend([""] * (10 - len(cells)))
        lines.append("| " + " | ".join(cells) + " |")

    lines.append("")
    lines.append("## Implemented Problems")
    lines.append("")
    header = ["Problem", "Difficulty", "Title"] + list(LANGUAGES.values())
    aligns = ["---:", "---:", "---"] + [":---:" for _ in LANGUAGES]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(aligns) + "|")

    for p in problems:
        if not p.implemented:
            continue
        title = p.title if p.title else "—"
        lang_cells = [checkbox(p.langs.get(lang, False)) for lang in LANGUAGES]
        row = [
            f"[{p.number:03d}](https://projecteuler.net/problem={p.number})",
            f"{p.level} [{p.percent}]",
            title,
            *lang_cells,
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def update_readme(problems: list[Problem]) -> None:
    dashboard = render_dashboard(problems)

    if README_PATH.exists():
        old = README_PATH.read_text(encoding="utf-8")
    else:
        old = "# Project Euler Progress\n\n"

    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        flags=re.S,
    )

    if pattern.search(old):
        new = pattern.sub(dashboard, old)
    else:
        new = old.rstrip() + "\n\n" + dashboard + "\n"

    README_PATH.write_text(new + "\n", encoding="utf-8")


def show_problem(p: Problem) -> None:
    print()
    print(f"Problem {p.number:03d}")
    print(f"Title: {p.title or '—'}")
    print(f"Difficulty: {p.level} [{p.percent}]")
    print(f"Project Euler account solved: {checkbox(p.euler_solved)}")
    for lang, label in LANGUAGES.items():
        print(f"{label}: {checkbox(p.langs.get(lang, False))}")
    print()


def edit_problem(problems: list[Problem]) -> None:
    raw = input("Problem number: ").strip()
    if not raw.isdigit():
        print("Not a number.")
        return

    n = int(raw)
    if not (1 <= n <= len(problems)):
        print("Out of range.")
        return

    p = problems[n - 1]

    while True:
        show_problem(p)
        print("Toggle:")
        print("  e  Project Euler solved")
        for key, label in LANGUAGES.items():
            print(f"  {key:<4} {label}")
        print("  t  title")
        print("  d  difficulty")
        print("  q  back")
        choice = input("> ").strip().lower()

        if choice == "q":
            save_state(problems)
            return
        if choice == "e":
            p.euler_solved = not p.euler_solved
        elif choice in LANGUAGES:
            p.langs[choice] = not p.langs.get(choice, False)
        elif choice == "t":
            p.title = input("Title: ").strip()
        elif choice == "d":
            p.level = input("Level, e.g. L02: ").strip() or p.level
            p.percent = input("Percent, e.g. 7%: ").strip() or p.percent
        else:
            print("Unknown option.")


def list_implemented(problems: list[Problem]) -> None:
    implemented = [p for p in problems if p.implemented]
    if not implemented:
        print("No implemented problems yet.")
        return

    for p in implemented:
        langs = ", ".join(
            label for key, label in LANGUAGES.items() if p.langs.get(key, False)
        )
        print(f"{p.number:03d}  {p.level} [{p.percent}]  {langs:15}  {p.title}")


def main() -> None:
    problems = load_state()

    while True:
        implemented = sum(p.implemented for p in problems)
        euler_solved = sum(p.euler_solved for p in problems)

        print()
        print("Project Euler README TUI")
        print("========================")
        print(f"Project Euler solved : {euler_solved}/{len(problems)}")
        print(f"Repo implemented     : {implemented}/{len(problems)}")
        print()
        print("1. Edit problem")
        print("2. List implemented problems")
        print("3. Regenerate README")
        print("4. Save state")
        print("5. Quit")
        choice = input("> ").strip()

        if choice == "1":
            edit_problem(problems)
        elif choice == "2":
            list_implemented(problems)
        elif choice == "3":
            save_state(problems)
            update_readme(problems)
            print(f"Updated {README_PATH}")
        elif choice == "4":
            save_state(problems)
            print(f"Saved {STATE_PATH}")
        elif choice == "5":
            save_state(problems)
            return
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
