def solution(s):
    p = s.lower() .count("p")
    y = s.lower() .count("y")
    return True if p == y else False