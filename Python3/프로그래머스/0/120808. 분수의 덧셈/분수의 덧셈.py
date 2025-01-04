from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]