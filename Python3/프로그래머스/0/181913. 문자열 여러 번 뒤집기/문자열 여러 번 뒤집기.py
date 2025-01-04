def solution(my_string, queries):
    answer = list(my_string)
    
    for start, end in queries:
        answer[start: end + 1] = answer[start: end + 1][::-1]

    return ''.join(answer)