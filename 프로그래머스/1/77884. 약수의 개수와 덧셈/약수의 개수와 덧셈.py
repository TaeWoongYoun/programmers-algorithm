def solution(left, right):
    answer = 0
    div = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div % 2 == 0:
            answer += i
        else:
            answer -= i
        div = 0
    return answer