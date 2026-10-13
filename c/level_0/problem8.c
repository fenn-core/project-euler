#include "perf.h"
#include <stdint.h>
#include <stdio.h>


const char digits[] =
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450";


uint64_t problem8_brute_force(void) {
    int length = 0;
    uint64_t product = 1UL;
    uint64_t max_value = 0;

    while (digits[length] != '\0') {
        ++length;
    }

    for (int i = 0; i < (length - 12); ++i) {
        for (int j = 0; j < 13; ++j) {
            if ((digits[i + j] - '0') == 0) {
                goto skip_multi;
            }
            product *= (digits[i + j] - '0');
        }
        if (product > max_value) {
            max_value = product;
        }
    skip_multi:
        product = 1UL;
    }

    return max_value;
}


uint64_t problem8_sliding_window(void) {
    int length = 0;
    uint64_t product = 1UL;
    uint64_t max_value = 0;
    int zero_count = 0;

    while (digits[length] != '\0') {
        ++length;
    }

    for (int i = 0; i < 13; ++i) {
        if ((digits[i] - '0') == 0) {
            ++zero_count;
        } else {
            product *= digits[i] - '0';
        }
    }
    if (zero_count == 0) {
        max_value = product;
    }

    for (int j = 0; j < (length - 13); ++j) {
        if ((digits[j + 13] - '0') == 0) {
            ++zero_count;
        } else {
            product *= (digits[j + 13] - '0');
        }

        if ((digits[j] - '0') != 0) {
            product /= (digits[j] - '0');
        } else {
            --zero_count;
        }

        if (zero_count == 0 && product > max_value) {
            max_value = product;
        }
    }

    return max_value;
}


/*
 * Strangely enough, using the CMake Debug configuration,
 * sliding window significantly outperforms brute force,
 * as expected. However, in Release, the results reverse.
 *
 * This is largely due to aggressive compiler optimizations:
 *
 * - The brute-force inner loop is completely unrolled,
 *   eliminating loop-control overhead.
 *
 * - Windows containing zero are skipped before performing
 *   the multiplications.
 *
 * - Conditional moves cmov replace branches when updating
 *   the maximum product.
 *
 * - Intermediate values are kept in registers, minimizing
 *   memory accesses.
 *
 * Meanwhile, the sliding-window implementation still requires
 * a relatively expensive 64 bit divq instruction for
 * each window, whereas brute force uses cheaper multiplications.
 *
 * Since the window size is fixed at just 13 digits, the
 * optimized O(13n) brute-force implementation can outperform the
 * O(n) sliding-window algorithm.
 *
 */


int main(void) {
    uint64_t (*volatile problem8_brute_force_ptr)(void) = &problem8_brute_force;
    BENCHMARK(ITERATIONS, "brute force", problem8_brute_force_ptr);

    uint64_t (*volatile problem8_sliding_window_ptr)(void) = &problem8_sliding_window;
    BENCHMARK(ITERATIONS, "sliding window", problem8_sliding_window_ptr);

    printf("expected result: 23514624000\n");

    return 0;
}
