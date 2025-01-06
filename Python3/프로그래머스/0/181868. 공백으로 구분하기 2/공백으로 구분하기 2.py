def solution(my_string):
    answer = []
    my_string = my_string.split(' ')
    for i in my_string:
        if i not in "":
            answer.append(i)
    return answer