def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        if numLog[i - 1] == numLog[i] + 1:
            answer += "s"
        elif numLog[i - 1] == numLog[i] - 1:
            answer += "w"
        elif numLog[i - 1] == numLog[i] + 10:
            answer += "a"
        elif numLog[i - 1] == numLog[i] - 10:
            answer += "d"
    return answer