def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer = answer * 2
    return answer