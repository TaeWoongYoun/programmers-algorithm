def solution(name, yearning, photo):
    answer = []

    for p in photo:
        total = 0
        for n, y in zip(name, yearning):
            for i in p:
                if i == n:
                    total += y
        answer.append(total)

    return answer