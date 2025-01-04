def solution(arr):
    result = arr[0]
    
    for i in range(1, len(arr)):
        a = result
        b = arr[i]
        while b:            
            a, b = b, a % b #유클리드 호제법
        result = result * arr[i] // a
    
    return result