def solution(array, commands):
    answer, a, b, c, li = [], [], [], [], []
    
    for i in commands:
        a.append(i[0])
        b.append(i[1])
        c.append(i[2])
    
    for j in range(0, len(a)):
        num = sorted(array[a[j]-1:b[j]])
        li.append(num[c[j] - 1])
        num = []
    
    return li