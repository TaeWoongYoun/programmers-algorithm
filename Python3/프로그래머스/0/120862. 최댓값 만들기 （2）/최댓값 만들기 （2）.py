def solution(numbers):
    return max([numbers[i] * numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i != j])