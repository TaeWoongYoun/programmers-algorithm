def solution(emergency):
    answer = []
    lis = sorted(emergency)
    lis.reverse()
    for i in emergency:
        answer.append(lis.index(i)+1)
    return answer