def solution(arr, query):
    for q in range(len(query)): arr = arr[:query[q] + 1] if q % 2 == 0 else arr[query[q]:]
    return arr