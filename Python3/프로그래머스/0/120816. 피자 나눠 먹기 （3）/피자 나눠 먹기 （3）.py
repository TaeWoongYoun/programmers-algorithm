def solution(slice, n):
    answer = 0
    for i in range(0, n):
        if slice * i < n:
            answer += 1
    return answer