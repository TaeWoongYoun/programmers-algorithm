def solution(my_string, is_prefix):
    answer = ""
    for i in my_string:
        if answer == is_prefix:
            return 1
        answer += i
    return 0