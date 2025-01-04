def solution(num_list):
    plus = sum(num_list) ** 2
    mul = 1
    
    for num in num_list:
        mul *= num   
    
    return int(mul < plus)