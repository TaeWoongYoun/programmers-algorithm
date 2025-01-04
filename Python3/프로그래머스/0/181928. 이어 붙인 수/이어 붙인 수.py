def solution(num_list):
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 1:
            even.append(i)
        else:
            odd.append(i)
    even = ''.join(map(str, even))   
    odd = ''.join(map(str, odd))
    return int(even) + int(odd)