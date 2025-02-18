def solution(quiz):
    answer = []
    for i in quiz:
        left, right = i.split("=")
        answer.append("O") if eval(left.strip()) == eval(right.strip()) else answer.append("X")
    return answer