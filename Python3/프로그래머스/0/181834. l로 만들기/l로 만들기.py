def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'l'*11))