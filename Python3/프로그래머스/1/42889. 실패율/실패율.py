def solution(N, stages):
    answer = []
    clear = len(stages)
    prev_count = 0
    index = []
    result = []
    for i in range(1, N+1):
        count = 0
        for j in stages:
            if i == j:
                count += 1
        clear = clear - prev_count
        prev_count = count
        if count != 0:
            answer.append(count / clear)
        else:
            answer.append(0)        
    for i in range(len(answer)):
        index.append([answer[i], i+1])
    index.sort(key=lambda x: x[1])
    index.sort(key=lambda x: x[0], reverse=True)  
    for i, j in index:
        result.append(j)
    return result