def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score) - len(score) % m, m):
        answer += min(score[i:i + m]) * m

    return answer
