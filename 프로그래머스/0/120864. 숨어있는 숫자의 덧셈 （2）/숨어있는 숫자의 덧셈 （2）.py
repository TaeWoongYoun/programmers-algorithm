import re

def solution(my_string):
    return sum(list(map(int,re.findall(r'\d+', my_string))))