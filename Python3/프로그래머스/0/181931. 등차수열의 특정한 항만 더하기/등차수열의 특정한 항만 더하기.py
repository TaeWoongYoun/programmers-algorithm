def solution(a, d, included):
    answer = 0
    for i in included:
        if i == True:
            answer += a
        a = a + d
    return answer