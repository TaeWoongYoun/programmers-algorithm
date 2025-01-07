def solution(arr, intervals):
    answer = []
    for i in intervals:
        f, s = i
        for j in range(f, s+1):
            answer.append(arr[j])
    return answer