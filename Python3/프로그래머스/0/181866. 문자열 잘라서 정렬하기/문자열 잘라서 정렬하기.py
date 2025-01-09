def solution(myString):
    myString = myString.split("x")
    myString.sort()
    myString = ' '.join(myString).split()
    return myString