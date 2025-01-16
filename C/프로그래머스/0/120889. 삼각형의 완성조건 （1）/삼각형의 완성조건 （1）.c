#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int sides[], size_t sides_len) {
    int answer = 0;
    
    for(int i=0;i<3;i++){
        if(sides[i]>sides[i+1])
        {
            int temp=sides[i];
            sides[i]=sides[i+1];
            sides[i+1]=temp;
        }
    }
    
    if(sides[0]+sides[1]>sides[2])
    {
        answer=1;
    }
    else
    {
        answer=2;
    }
    return answer;
}