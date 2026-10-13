#include "perf.h"
#include <math.h>
#include <stdio.h>
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
    BENCHMARK(ITERATIONS, "brute force", problem9_brute_force_ptr);

    int (*volatile problem9_optimized_search_ptr)(void) = &problem9_optimized_search;
    BENCHMARK(ITERATIONS, "optimized search", problem9_optimized_search_ptr);

    printf("expected result: 31875000 \n");

    return 0;
}
