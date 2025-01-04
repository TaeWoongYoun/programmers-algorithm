def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer