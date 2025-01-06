#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int i = 0;
    for (i = 1; i < n+1; i++){
        if (n % i == 0){
            answer += i;
        }
    }
    
    return answer;
}