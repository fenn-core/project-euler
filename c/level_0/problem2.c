#include "perf.h"
#include <stdio.h>


int main(void) {

    double initial_time = perf_counter();

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

    double elapsed_time = perf_counter() - initial_time;

    printf("%d \n", total);
    printf("%f \n", elapsed_time);

    return 0;

}