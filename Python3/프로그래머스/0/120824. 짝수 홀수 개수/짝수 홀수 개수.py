def solution(num_list):
    odd = []
    even = []
    
    for i in num_list:
        if i % 2 == 1:
            odd.append(i)
            
    for j in num_list:
        if j % 2 == 0:
            even.append(j)
    
    return [len(even), len(odd)]