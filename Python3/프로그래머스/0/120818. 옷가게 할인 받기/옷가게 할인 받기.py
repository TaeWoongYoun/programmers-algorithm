def solution(price):
    if 300000 > price >= 100000:
        return int(price - (price * 0.05))
    elif 500000 > price >= 300000:
        return int(price - (price * 0.1))
    elif price >= 500000:
        return int(price - (price * 0.2))
    return price