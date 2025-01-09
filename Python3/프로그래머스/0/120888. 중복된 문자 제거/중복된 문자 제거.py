def solution(my_string):
    return "".join(list(dict.fromkeys(my_string)))