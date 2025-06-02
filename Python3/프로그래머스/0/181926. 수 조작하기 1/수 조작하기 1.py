def solution(n, control):
    for i in control: n += {"w": 1,"s": -1,"d": 10,"a": -10}[i]
    return n