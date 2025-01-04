def solution(wallpaper):
    x, y = set(), set()

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x.add(i)
                y.add(j)
    
    print(x, y)
    return [min(x), min(y), max(x) + 1, max(y) + 1]
