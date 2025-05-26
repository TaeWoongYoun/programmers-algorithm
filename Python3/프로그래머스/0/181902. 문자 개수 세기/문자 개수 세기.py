def solution(my_string):
    answer = []
    for i in range(65, 91): 
        answer.append(my_string.count(chr(i))) if chr(i) in my_string else answer.append(0)
    for j in range(97, 123): 
        answer.append(my_string.count(chr(j))) if chr(j) in my_string else answer.append(0)
    return answer