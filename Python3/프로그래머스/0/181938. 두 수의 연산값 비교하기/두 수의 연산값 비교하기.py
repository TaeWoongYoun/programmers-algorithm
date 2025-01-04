def solution(a, b):
    var = int(str(a) + str(b)) 
    var2 = 2 * a * b

    if var >= var2 :
        return var
    else :
        return var2