def solution(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
        if answer > n:
            return i - 1
    return i