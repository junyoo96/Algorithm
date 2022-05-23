# 9:22 ~ 9:50
# 10:00 ~ 10:27

def solution(N, stages):
    # n : 전체 스테이지 수
    # stages : 사용자가 현재 멈춰있는 스테이지 번호 리스트

    answer = []  # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 리스트
    length = len(stages)  # stages 크기
    failures = []  # 실패율 리스트(실패율, 스테이지 번호)

    # 스테이지 수 반복하면서
    for i in range(1, N + 1):

        cnt = stages.count(i) # 해당 스테이지에 머물러 있는 사람의 수 계산

        # 실패율 계산
        if length == 0:
            percentage = 0
        else:
            percentage = cnt / length

        # failures에 (실패율, 스테이지 번호) 추가
        failures.append((percentage, i))
        # length를 cnt만큼 감소
        length -= cnt

    # failures 실패율 기준으로 내림차순, 같으면 스테이지 번호기준으로 오름차순 정렬
    failures.sort(key=lambda x: (-x[0], x[1]))

    # failures 반복하면서 answer에 스테이지 번호 추가
    answer = [failure[1] for failure in failures]

    return answer
