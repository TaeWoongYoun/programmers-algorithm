def solution(n):
    answer = ''
    for i in range(1, n+1):
        answer += "박" if i % 2 == 0 else "수"
    return answer