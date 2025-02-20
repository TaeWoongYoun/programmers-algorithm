import datetime

def solution(a, b):
    return ['MON','TUE','WED','THU','FRI','SAT','SUN'][datetime.date(2016,a,b).weekday()]