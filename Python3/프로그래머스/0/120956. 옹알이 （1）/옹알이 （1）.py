def solution(babbling):
    a = ["aya","ye","woo","ma"]
    answer = 0
    for i in babbling:
        result = 0
        for j in range(4):
            if i.find(a[j]) != -1:
                result += len(a[j])
        if len(i) == result:
            answer += 1
        
    return answer