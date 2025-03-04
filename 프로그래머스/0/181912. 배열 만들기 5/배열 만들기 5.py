def solution(intStrs, k, s, l):
    answer = []
    result = []
    for i in range(len(intStrs)):
        answer.append(intStrs[i][s:s+l])
    for j in range(len(answer)):
        if int(answer[j]) > k:
            result.append(int(answer[j]))
    return result