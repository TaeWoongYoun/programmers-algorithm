import re

def solution(my_string):
    return sorted(list(map(int, re.sub(r'[^0-9]', '', my_string))))