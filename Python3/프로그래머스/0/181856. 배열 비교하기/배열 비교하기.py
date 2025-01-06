def solution(arr1, arr2):
    if len(arr1) > len(arr2) or len(arr1) == len(arr2) and sum(arr1) > sum(arr2):
        return 1
    elif len(arr1) < len(arr2) or len(arr1) == len(arr2) and sum(arr1) < sum(arr2):
        return -1
    else:
        return 0