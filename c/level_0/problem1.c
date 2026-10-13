#include "perf.h"
#include <stdio.h>


int problem1(void) {
    int total = 0;
    for (int i = 0; i < 1000; ++i) {
        if ((i % 5 == 0) || (i % 3 == 0)) {
            total += i;
        }
    }
}


int main(void) {
    int (*volatile problem1_ptr)(void) = &problem1;
    BENCHMARK(ITERATIONS, "", problem1_ptr);

    printf("expected result: 4195632");


    return 0;

}