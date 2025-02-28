def solution(s):
    answer = ''
    index = 0
    for i in s:
        if i == ' ':
            answer += ' '
            index = 0
        else:
            if index % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            index += 1
    return answer