#include "perf.h"
#include <stdio.h>
#include <math.h>
#include <stdint.h>


int problem9_brute_force(void) {
    /*
     * The floating point comparison here is acceptable
     * although its not generally valid
    */

    double c = 0;

    for (int b = 0; b < 500; ++b) {
        for (int a = 0; a < b; ++a) {
            c = sqrt((a * a) + (b * b));
            if (a + b + c == 1000) {
                return a * b * (int) c;
            }
        }
    }
    return 0;
}


int problem9_optimized_search(void) {
    int a = 0;
    int numerator = 0;
    int denominator = 0;

    for (int b = 500; 0 < b; --b) {
        numerator = (1000 * (500 - b));
        denominator = (1000 - b);

        if (numerator % denominator != 0) {
            continue;
        }
        a = numerator / denominator;
        if (b > a && a > 0) {
            return a * b * (1000 - a - b);
        }
    }
    return 0;
}


int main(void) {
    int (*volatile problem9_brute_force_ptr)(void) = &problem9_brute_force;
    uint64_t brute_force_checksum = 0;

    double brute_force_initial = perf_counter();

    for (size_t iters = 0; iters < ITERATIONS; ++iters) {
        brute_force_checksum += problem9_brute_force_ptr();
    }

    double brute_force_elapsed = perf_counter() - brute_force_initial;
    int brute_force_result = (int) (brute_force_checksum / ITERATIONS);

    printf("brute force average: %.3f us\n", brute_force_elapsed * 1e6 / ITERATIONS);
    printf("brute force result: %d\n\n", brute_force_result);


    int (*volatile problem9_optimized_search_ptr)(void) = &problem9_optimized_search;
    uint64_t optimized_search_checksum = 0;

    double optimized_search_initial = perf_counter();

    for (size_t iters = 0; iters < ITERATIONS; ++iters) {
        optimized_search_checksum += problem9_optimized_search_ptr();
    }

    double optimized_search_elapsed = perf_counter() - optimized_search_initial;
    int optimized_search_result = (int) (optimized_search_checksum / ITERATIONS);

    printf("optimized search average: %.3f us\n", optimized_search_elapsed * 1e6 / ITERATIONS);
    printf("optimized search result: %d\n\n", optimized_search_result);


    printf("expected result: 31875000 \n");

    return 0;
}
