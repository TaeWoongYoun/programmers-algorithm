def solution(people, limit):
    people.sort()
    count = 0
    a, b = 0, len(people) - 1
    while a <= b:
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1
        count += 1
    return count