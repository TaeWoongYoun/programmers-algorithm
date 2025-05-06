def solution(array):
    counts = {}
    max_count = 0
    answer = 0
    
    for i in array:
        counts[i] = counts.get(i, 0) + 1
        if counts[i] > max_count:
            max_count = counts[i]
            answer = i
        elif counts[i] == max_count:
            answer = -1
            
    return answer
