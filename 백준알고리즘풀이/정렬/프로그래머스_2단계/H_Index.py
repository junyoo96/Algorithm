# 3:00~3:40/3:40~4:00
# 최적화 코드
def solution(citations):
    citations.sort(reverse=True)
    '''
    1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
    2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분으로 생각하시면 됩니다. 예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1(해당 인용수 이상의 논문개수를 의미), 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 
    즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출),이고
    max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법
    '''
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

#=========================================================
# 내 코드 - 이진탐색 사용
# n : 발표한 논문
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최대값이 과학자의 h-index
from bisect import bisect_left

def solution(citations):
    answer = 0

    # 정렬
    length = len(citations)
    citations.sort()

    end = citations[-1]
    for h in range(end, -1, -1):
        # h로 인용횟수 논문들이 나뉘는 기준 idx 찾기
        idx = bisect_left(citations, h)
        # h이상 인용횟수 논문 개수
        up = length - idx
        # h이하 인용횟수 논문 개수
        down = length - up

        if up >= h and down <= h:
            answer = h
            break

    return answer