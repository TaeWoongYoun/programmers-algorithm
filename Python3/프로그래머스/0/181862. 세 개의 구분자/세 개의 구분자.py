def solution(myStr):
    answer = []
    st = ""
    for i in myStr:
        if i not in ["a", "b", "c"]:
            st += i
        else:
            if st == "":
                continue
            else:
                answer.append(st)
            st = ""
    if st:
        answer.append(st)
    if not answer:
        return ["EMPTY"]
    else:
        return answer