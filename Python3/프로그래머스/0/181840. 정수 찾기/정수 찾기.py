def solution(num_list, n):
    if str(n) in list(map(str, num_list)):
        return 1
    else:
        return 0