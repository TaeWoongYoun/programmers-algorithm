def solution(operations):
    answer = []
    for i in operations:
        str = i.split(" ")
        if str[0] == "I":
            answer.append(int(str[1]))
        elif str[0] == "D":            
            if not answer:
                continue
            elif str[1] == "1":
                answer.remove(max(answer))
            elif str[1] == "-1":
                answer.remove(min(answer))
    if not answer:
        return [0,0]
    else:
        return [max(answer), min(answer)]