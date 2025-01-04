def solution(x):
    answer = False
    sum_x = sum(map(int, str(x)))
    
    if x % sum_x == 0:
        answer = True
                
    return answer