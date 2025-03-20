#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    if(n % 7 == 0) return n / 7;
    return n / 7 + 1;
}