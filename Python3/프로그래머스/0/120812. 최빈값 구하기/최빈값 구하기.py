def solution(array):
    max_cnt, answer = 0, 0
    for i in set(array):
        cnt = array.count(i)
        if cnt > max_cnt: 
            max_cnt, answer = cnt, i
        elif cnt == max_cnt: 
            answer = -1
    return answer