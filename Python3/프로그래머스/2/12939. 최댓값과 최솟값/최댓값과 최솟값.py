def solution(s):
    numbers = list(map(int, s.split()))
    
    minimum = min(numbers)
    maximum = max(numbers)
    
    # if minimum > maximum:
    #     answer = f"{maximum} {minimum}"
    # else:
    #     answer = 

    return f"{minimum} {maximum}"