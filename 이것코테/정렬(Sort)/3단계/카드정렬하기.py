#11:00~11:10
#11:10~

# 최적해 아이디어 : 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장

# 카드 묶음 크기를 넣을 때 카드 묶음 크기 순서대로 정렬하기 위해 우선순위 큐 heapq 사용
import heapq

answer = 0 # 최소 몇번의 비교가 필요한지 비교 수
n = int(input()) # 숫자 카드 묵음 개수

# heap에 초기 카드 묶음을 모두 삽입
heap = []
for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)

# heap에 카드 묶음이 하나만 남을 때까지 반복하면서
while len(heap) != 1:
    # 가장 작은 카드 크기 묶음 꺼내기
    card_one = heapq.heappop(heap)
    # 그다음으로 작은 카드 크기 묶음 꺼내기
    card_two = heapq.heappop(heap)
    # 비교 수 계산
    sum_value = card_one + card_two
    # 비교 수 더하기
    answer += sum_value
    # 합친 카드 묶음 다시 삽입
    heapq.heappush(heap, sum_value)

print(answer)