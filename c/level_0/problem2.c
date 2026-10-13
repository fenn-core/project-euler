#include "perf.h"
#include <stdio.h>


int problem2(void) {
    int a = 0;
    int b = 1;
    int total = 0;
    while (b < 4000000) {
        if (b % 2 == 0) {
            total += b;
        }
        int next = a + b;
        a = b;
        b = next;
    }
}


int main(void) {
    int (*volatile problem2_ptr)(void) = &problem2;
    BENCHMARK(ITERATIONS, "", problem2_ptr);

    printf("expected result: 5702887");

    return 0;

}