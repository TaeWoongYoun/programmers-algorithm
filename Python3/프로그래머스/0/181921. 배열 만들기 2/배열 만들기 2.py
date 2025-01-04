def not_num(num):
    for digit in '12346789':
        if digit in str(num): 
            return False       
    return True
    

def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if not_num(i):
            answer.append(i)
            
    if answer == []:
        return [-1]
    
    return answer

# def solution(l, r):
#     return [num for num in range(l, r+1) if '5' in str(num) and '0' in str(num)]