#include "perf.h"
#include <stdio.h>

int main(void) {
    double initial_time = perf_counter();

    int total = 0;

    for (int i = 0; i < 1000; ++i) {

        if ((i % 5 == 0) || (i % 3 == 0)) {
            total += i;
        }
    }

    double elapsed_time = perf_counter()-initial_time;

    printf("%d\n", total);
    printf("%f\n", elapsed_time);


    return 0;

}