def solution(A,B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])