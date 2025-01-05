def solution(my_strings, parts):
    answer = ''
    for i, j in zip(my_strings, parts):
        f, s = j
        answer += i[f:s+1]
    return answer