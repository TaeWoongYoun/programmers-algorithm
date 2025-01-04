def solution(t, p):
    answer = []
    
    for i in range(len(t) - len(p) + 1):
        new_t = t[i:i + len(p)]
        if p >= new_t:
            answer.append(new_t)
            
    return len(answer)