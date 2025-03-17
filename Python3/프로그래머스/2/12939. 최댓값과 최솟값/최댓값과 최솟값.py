def solution(s):
    numbers = list(map(int, s.split()))
    
    minimum = min(numbers)
    maximum = max(numbers)

    return f"{minimum} {maximum}"