def solution(my_string, overwrite_string, s):

    var = my_string[:s]
    var2 = overwrite_string
    var3 = my_string[s + len(overwrite_string):]
    answer = var + var2 + var3
    return answer