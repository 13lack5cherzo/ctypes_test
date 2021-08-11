#include <stdio.h>
#include <string.h>
#include <ctype.h>

int square(int i) {
    return i * i;
}

float multiply(float f1, float f2, float f3) {
    return f1 + f2 * f3;
}

void caps(char *input) {
    for (int ii=0; ii < strlen(input); ii++) {
        input[ii] = toupper(input[ii]);
    }
}

float dot_prod(float *a1, int a1_size, float *a2, int a2_size) {

    // check that arrays are the same size
    if (a1_size != a2_size) {
        return 0;
    }
    float sum1 = 0;  // initialise sum
    for (int i=0; i < a1_size; i++) {  // for every element,
        sum1 += a1[i] * a2[i];  // add to cumulative sum
    }
    return sum1;
}

float *return_a(float *a1) {
    return a1;
}

float *hadamard_1d(float *a1, int a1_size, float *a2, int a2_size, float *a_out) {
    // check that arrays are the same size
    if (a1_size != a2_size) {
        return a1;
    }
    // hadamard product
    for (int i=0; i < a1_size; i++) {
        a_out[i] = a1[i] * a2[i];
    }
    return a_out;
}

int main(void) {
    return 0;
}

// cc -Wall -o cfuncs cfuncs.c
// cc -fPIC -shared -o cfuncs.so cfuncs.c