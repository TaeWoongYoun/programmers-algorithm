def solution(n, k):
    answer = []

    for i in range(k, n+1):
        if i % k == 0: 
            answer.append(i) 

    return answer
