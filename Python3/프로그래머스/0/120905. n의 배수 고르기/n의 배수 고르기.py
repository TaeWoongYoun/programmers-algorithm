def solution(n, numlist):
    answer = []
    num = 0
    for i in numlist:
        num = i / n
        if float(num).is_integer():
            answer.append(i)
    return answer