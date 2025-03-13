def solution(strArr):
    answer = []
    cnt = []
    for i in strArr:
        answer.append(len(i))
    for i in range(1, max(answer)+1):
        cnt.append(answer.count(i))
    return max(cnt)