
def solution(s):
    
    p = s.lower() .count("p")
    y = s.lower() .count("y")
    if p == y:
        return True
    else:
        return False