def solution(myString, pat):
    pat = pat.lower()
    myString = myString.lower()
    return 1 if pat in myString else 0