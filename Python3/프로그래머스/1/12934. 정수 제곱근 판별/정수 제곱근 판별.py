import math

def solution(n):
    if ((int(n ** 0.5) ** 2 == n)*1) == 1:
        return (math.sqrt(n) + 1) ** 2
    else:
        return -1