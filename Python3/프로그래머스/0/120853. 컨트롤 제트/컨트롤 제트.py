def solution(s):
    answer = []
    s = s.split()
    for i in s:
        if i == "Z":
            answer.pop()
        else:
            answer.append(i)
    answer = list(map(int, answer))
    return sum(answer)