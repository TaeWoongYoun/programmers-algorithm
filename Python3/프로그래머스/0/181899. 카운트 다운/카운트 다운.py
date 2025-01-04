def solution(start_num, end_num):
    answer = []
    num = start_num - end_num
    for i in range(num+1):
        answer.append(start_num - i)
    return answer