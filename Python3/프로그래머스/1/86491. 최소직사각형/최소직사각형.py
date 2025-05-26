def solution(sizes):
    num1, num2, li = [], [], []
    for s in sizes:
        li.append([max(s), min(s)])
    
    for i in li:
        num1.append(i[0])
        num2.append(i[1])
    return max(num1) * max(num2)