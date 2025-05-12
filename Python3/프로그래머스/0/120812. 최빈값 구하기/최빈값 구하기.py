def solution(array):
    max_count, answer = 0, 0
    for i in set(array):
        count = array.count(i)
        if count > max_count: 
            max_count, answer = count, i
        elif count == max_count: 
            answer = -1
    return answer