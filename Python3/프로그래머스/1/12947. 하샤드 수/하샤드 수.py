def solution(x):
    return True if x % sum(map(int, str(x))) == 0 else False