def solution(my_string):
    answer = []
    for i in range(65, 91):
        if chr(i) in my_string:
            answer.append(my_string.count(chr(i)))
        else:
            answer.append(0)
    for j in range(97, 123):
        if chr(j) in my_string:
            answer.append(my_string.count(chr(j)))
        else:
            answer.append(0)
    return answer