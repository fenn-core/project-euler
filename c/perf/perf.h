#ifndef PROJECT_EULER_PERF_H
#define PROJECT_EULER_PERF_H

#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>

#define ITERATIONS  100000

#define BENCHMARK(benchmark_iters, name, func_ptr, ...) \
    do { \
    int64_t _benchmark_sum = 0; \
    double _initial = perf_counter(); \
    for (size_t _i = 0; _i < benchmark_iters; ++_i) \
    {_benchmark_sum += (func_ptr)(__VA_ARGS__);} \
    double _elapsed = perf_counter() - _initial; \
    printf("%s average: %.3f us\n", name, _elapsed * 1e6 / benchmark_iters); \
    printf("%s result: %" PRIi64 "\n\n", name, (_benchmark_sum / (benchmark_iters))); \
} while (0)


double perf_counter(void);

#endif //PROJECT_EULER_PERF_H
