def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1+y2)+(x3+x4) == (y3+y4)+(x1+x2))
    answer2 = ((y1+y3)+(x2+x4) == (y2+y4)+(x1+x3))
    answer3 = ((y1+y4)+(x2+x3) == (y2+y3)+(x1+x4))
    
    if answer1 or answer2 or answer3:
        return 1
    else:
        return 0
    