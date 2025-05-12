def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            i = i // 2 if i % 2 == 0 else (i - 1) // 2
            answer += 1
    return answer