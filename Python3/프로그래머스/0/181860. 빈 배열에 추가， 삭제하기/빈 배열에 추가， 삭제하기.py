def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i] * 2)
        else:
            del answer[-arr[i]:]
    return answer