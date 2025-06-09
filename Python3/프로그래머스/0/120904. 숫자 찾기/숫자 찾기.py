def solution(num, k):
    return list(str(num)).index(str(k)) + 1 if str(k) in str(num) else -1