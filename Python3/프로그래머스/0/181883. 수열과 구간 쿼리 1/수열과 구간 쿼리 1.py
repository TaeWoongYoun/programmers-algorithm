def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
            
    return arr