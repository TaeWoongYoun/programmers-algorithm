def solution(s):
    answer = [ord(i) for i in s]
    answer.sort(reverse=True)
    answer = ''.join(chr(i) for i in answer)
    
    return answer