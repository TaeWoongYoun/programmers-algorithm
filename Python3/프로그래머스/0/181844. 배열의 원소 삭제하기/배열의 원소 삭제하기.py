def solution(arr, delete_list):
    for i in arr[:]: #리스트 복사본 만들기
        for j in delete_list:
            if i == j:
                arr.remove(i)
    return arr