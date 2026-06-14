#include "perf.h"
#include <stdio.h>


int main () {
    double intial_time = perf_counter();

    int sum_of_squares = 0;
    int square_of_sum = 0;
    for (int i = 1; i <= 100; ++i) {
        square_of_sum += i;
        sum_of_squares += (i * i);
    }
    square_of_sum = square_of_sum * square_of_sum;
    int ans = square_of_sum - sum_of_squares;

    double elapsed_time = perf_counter() - intial_time;

    printf("%d \n", ans);
    printf("%f \n", elapsed_time);

    return 0;

}