#include "perf.h"
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

#undef ITERATIONS
#define ITERATIONS  500


bool is_bouncy(unsigned int num) {
    bool is_increasing = false;
    bool is_decreasing = false;

    while (num >= 10) {
        unsigned int num_tenth = num / 10U;
        uint64_t left = num_tenth % 10;
        unsigned int right = num % 10;

        if (right < left) {
            is_decreasing = true;
        }
        if (right > left) {
            is_increasing = true;
        }
        if (is_decreasing && is_increasing) {
            return true;
        }
        num = num_tenth;
    }
    return false;
}


int problem112(void) {
    int checked = 0;
    int bouncy = 0;

    for (unsigned int n = 1; ; ++n) {
        if (is_bouncy(n)) {
            ++bouncy;
        }
        ++checked;

        if (checked % 100 == 0) {
            if (checked * 99LL == bouncy * 100LL) {
                return checked;
            }
        }
    }
}


int main(void) {
    int (* volatile fn)(void) = &problem112;
    BENCHMARK(ITERATIONS, "", fn);

    printf("expected result: 1587000\n");

    return 0;
}
