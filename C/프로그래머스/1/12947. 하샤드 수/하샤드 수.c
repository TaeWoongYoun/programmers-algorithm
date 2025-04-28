#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    int sum = 0;
    for (int i = x; i != 0; i /= 10) {
        sum += (i % 10);
    }
    if (x % sum == 0) return true;
    else return false;
}