def solution(hp):
    answer = 0
    i = 0
    
    while hp > 0:
        if hp >= 5:
            hp -= 5
        elif hp >= 3:
            hp -= 3
        elif hp >= 1:
            hp -= 1
        i += 1
    
    answer = i
    return answer