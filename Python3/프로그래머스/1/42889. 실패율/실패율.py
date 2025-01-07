def solution(N, stages):
    rates = []  # [실패율, 스테이지] 저장할 리스트
    players = len(stages)  # 전체 플레이어 
    for stage in range(1, N+1):
        if players:  # 플레이어가 있을 때만 실패율 계산
            count = stages.count(stage)  # 현재 스테이지에 있는 플레이어 수
            rates.append([count/players, stage])
            players -= count
        else:  # 플레이어가 없으면 실패율 0
            rates.append([0, stage])
    rates.sort(key=lambda x: (-x[0], x[1]))  # 실패율 내림차순, 스테이지 오름차순
    return [stage for _, stage in rates]  # 스테이지 번호만 반환