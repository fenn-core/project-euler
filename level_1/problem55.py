from time import perf_counter

initial_time = perf_counter()


def reverse_sum(num):
    return num + int(str(num)[::-1])


def is_palindrome(num):
    return str(num)[::-1] == str(num)


def lychrel_counter(cap=10_000):
    lychrel_count = cap - 1
    for num in range(1, cap):
        for iters in range(50):
            num = reverse_sum(num)
            if is_palindrome(num):
                lychrel_count -= 1
                break

    return lychrel_count


print(lychrel_counter(10_000))

print(perf_counter() - initial_time)
