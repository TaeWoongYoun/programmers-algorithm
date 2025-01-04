from collections import Counter

def solution(k, tangerine):
    answer = []
    count = Counter(tangerine)
    new_tangerines = count.most_common()
    
    for tangerine, freq in new_tangerines:
        for i in range(freq):
            answer.append(tangerine)

    return len(list(set(answer[:k])))