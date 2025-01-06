def solution(myString):
    answer = [" " if i == "x" else i for i in myString]
    answer = "".join(answer)
    answer = answer.split(" ")
    return [len(i) for i in answer]