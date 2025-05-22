def solution(arr, queries):
    for q in queries:
        s, e = q
        for i in range(s, e + 1):
            if s <= i <= e:
                arr[i] += 1
            
    return arr