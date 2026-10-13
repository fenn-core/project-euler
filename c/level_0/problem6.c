#include "perf.h"
#include <stdio.h>


int problem6(void) {
    int sum_of_squares = 0;
    int square_of_sum = 0;
    for (int i = 1; i <= 100; ++i) {
        square_of_sum += i;
        sum_of_squares += (i * i);
    }
    square_of_sum = square_of_sum * square_of_sum;
    return square_of_sum - sum_of_squares;
}


int main(void) {
    int (*volatile problem6_ptr)(void) = &problem6;
    BENCHMARK(ITERATIONS, "", problem6);

    printf("expected result: 25164150");

    return 0;
}