def solution(n, control):

    new = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10,
    }
    
    for i in control:
        n += new[i]

    return n