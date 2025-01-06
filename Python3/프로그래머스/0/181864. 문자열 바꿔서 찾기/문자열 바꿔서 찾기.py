def solution(myString, pat):
    return int(pat in myString.replace("A","X").replace("B","A").replace("X","B"))