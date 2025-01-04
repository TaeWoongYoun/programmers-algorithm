def solution(n, m):
    answer = []
    minimum = []
    new_minimum = 0
    for i in range (1, n+1):
        if n % i == 0 and m % i == 0:
            answer = [i]
            
    for i in range (1, n*m+1):
        if i % n == 0 and i % m == 0:
            minimum.append(i)
            
    new_minimum = min(minimum)
    
    answer.append(new_minimum)
    return answer