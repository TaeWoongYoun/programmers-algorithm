def solution(n_str):
    n_str = list(n_str)
    while True:
        if n_str[0] == '0':
            n_str.remove('0')
        else:
            break
    return ''.join(n_str)