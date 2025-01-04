def solution(a, b, c):
    answer = a+b+c
    if a==b==c:
        answer = answer*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a==b or b==c or c==a:
        answer = answer*(a**2+b**2+c**2)
    return answer