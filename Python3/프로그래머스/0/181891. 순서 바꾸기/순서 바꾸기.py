def solution(num_list, n):
    return num_list if len(num_list) == n else sum([num_list[-(len(num_list)-n):], num_list[0:n]], [])