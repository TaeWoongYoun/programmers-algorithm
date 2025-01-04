def solution(lines):
    lines = [set(range(min(l), max(l))) for l in lines]
    return len(lines[0] & lines[1] | lines[0] & lines[2] | lines[1] & lines[2])