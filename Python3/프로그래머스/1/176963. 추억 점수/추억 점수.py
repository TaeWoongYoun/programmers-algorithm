def solution(name, yearning, photo):
    li = {}
    answer = []
    
    for i in range(len(name)):
        li[name[i]] = yearning[i]

    for j in photo:
        total = 0
        for k in j:
            if k in li:
                total += li[k]
        answer.append(total)

    return answer