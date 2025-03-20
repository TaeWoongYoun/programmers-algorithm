#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int array[], size_t array_len, int height) {
    int answer = 0;
    for(int i = 0; i < array_len; i++) {
        if (array[i] > height) {
            answer += 1;
        }
    }
    return answer;
}