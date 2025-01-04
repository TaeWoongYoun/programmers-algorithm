def solution(array):
    counts = {}
    max_count = 0
    answer = 0
    
    for num in array:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_count:
            max_count = counts[num]
            answer = num
        elif counts[num] == max_count:
            answer = -1
            
    return answer
