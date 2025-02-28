def solution(left, right):
    answer = 0
    div = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        answer += i if div % 2 == 0 else - i
        div = 0
    return answer