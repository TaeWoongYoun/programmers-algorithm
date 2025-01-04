def solution(n):
    f, s = 0, 1
    for i in range(2, n+1):
        f, s = s, f+s
    if n == 0:
        return 0
    return s % 1234567