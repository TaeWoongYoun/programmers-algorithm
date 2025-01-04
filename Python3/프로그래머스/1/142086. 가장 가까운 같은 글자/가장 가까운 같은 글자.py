def solution(s):
    answer = []

    for i in range(len(s)):
        find = False
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:  # 이전 위치에서 동일한 문자 찾기
                answer.append(i - j)  # 차이를 answer에 추가
                find = True
                break  # 동일한 문자 찾으면 반복문 종료
        if not find:
            answer.append(-1)

    return answer