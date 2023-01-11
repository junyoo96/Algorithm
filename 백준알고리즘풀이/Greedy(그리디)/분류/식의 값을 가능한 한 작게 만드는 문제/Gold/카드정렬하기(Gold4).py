# 9:37~9:47 / 9:47~10:06 (29분)
# # 12:01~12:24/12:24~12:26 (25분)

# A, B : 각 묶음의 카드 수
# 각 묶음을 합쳐서 하날 만드는데 A+B 비교횟수 필요
# answer : 최소한 몇 번의 비교가 필요한지
# 최적해 방안 : 카드 묶음이 수가 많은 묶음을 합치는 행위를 최대한 적게 해야하므로, 카드수를 기준으로 오름차순 정렬해서 순서대로 합치기
#======================================================================
# 개선 코드
import sys
import heapq
input = sys.stdin.reedline

n = int(input())
queue = [int(input()) for _ in range(n)]
# 개선 - heapify 사용
heapq.heapify(queue)

answer = 0
for _ in range(n - 1):
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)
    compare = first + second
    answer += compare
    heapq.heappush(queue, compare)

print(answer)
#======================================================================
# 내코드
import sys
import heapq

answer = 0
# n 입력
n = int(sys.stdin.readline())
# 각 카드 묶음 수 입력
queue = []
# 중요 - 묶을 때마다 항상 카드 수가 가장 적은 묶음끼리 묶어야 되므로, 큐에 맨앞에 항상 가장 적은 카드수를 보장하기 위해 우선순위 큐 사용
for _ in range(n):
    heapq.heappush(queue, int(sys.stdin.readline()))

# 카드 묶음 리스트 반복하면서
for _ in range(n - 1):
    # answer에 (이전 묶음에서 비교한횟수 + 현재 묶음 횟수) 더하기
    compare = heapq.heappop(queue) + heapq.heappop(queue)
    answer += compare
    heapq.heappush(queue, compare)

# answer 출력
print(answer)
