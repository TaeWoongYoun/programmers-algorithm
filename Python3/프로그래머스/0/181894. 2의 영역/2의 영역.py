def solution(arr):
    answer = []
    snum = -1
    fnum = len(arr)
    for i in arr:
        snum += 1
        if i == 2:
            break
    
    for j in range(len(arr)-1, -1, -1):
        fnum -= 1
        if arr[j] == 2:
            break
            
    if 2 not in arr:
        return [-1]
    else:
        return arr[snum:fnum+1]