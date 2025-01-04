def solution(my_string):
    my_string = my_string[::-1]
    answer = ""
    li = []
    for i in my_string:
        answer += i
        li.append(answer[::-1])
    li.sort()
    return li