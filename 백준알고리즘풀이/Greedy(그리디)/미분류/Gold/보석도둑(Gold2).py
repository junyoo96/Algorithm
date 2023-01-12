# 9:30~10:00 / 10:00~ 시간초과

# n : 보석 개수
# m, v : 무게, 가격
# k : 가방 개수
    # C : 각 가방에 담을 수 있는 최대 무게
    # 가방에는 한개의 보석만 넣을 수 있음
# answer : 상덕이가 훔칠 수 있는 보석의 최대 가격
# 최적해 방안 : 가방이 수용하는 무게가 아무리 커도 가방 1개에는 보석 1개만 담을 수 있으므로, 가방에 보석을 넣을때마다 가장 적은 무게를 수용하는 가방으로 가장 가격이 높은 보석을 수용하면 됨
#==============================================================================
# 정답 코드
#==============================================================================
import sys
import heapq

# 상덕이가 훔칠 수 있는 보석의 최대 가격
answer = 0
# 보석 개수, 가방 개수 입력
n, k = map(int, sys.stdin.readline().split())
# 보석 무게, 보석 가격 입력
jewels = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 가방에 담을 수 있는 최대 무게 입력
bags = [int(sys.stdin.readline()) for _ in range(k)]

# 무게 기준으로 보석 오름차순 정렬
jewels.sort()
# 무게 기준으로 가방 오름차순 정렬
bags.sort()

# 담을 수 있는 보석을 가치가 높은순으로 저장하는 우선순위큐로 사용하기 위해 사용
# 주의 - for문 안이 아니라 바깥에 있어야함, 이전 가방에서 체크했던 보석이라도 가방 용량이 오름차순 정렬되어 있으므로 다음가방에서 수용가능하기 때문에 남겨두어야함
tmp = []
# 가방을 반복하면서
for b in bags:
    # 보석이 남아있고 현재 보석의 무게가 현재 가방에 담을 수 무게보다 작거나 같은 경우
    while jewels and jewels[0][0] <= b:
        # 중요 - 현재 가방에 담을 수 있는 무게를 가진 보석들중 가장 가치가 높은 보석부터 담아야하므로 맨 앞에 가장 가치가 높은 보석을 보장하기 위해 우선순위 큐 사용
        # 하지만, python의 heap은 min_heap(오름차순으로 heap 추가)이기 때문에 -를 붙여서 제일 큰 가치를 제일 작은 가치로 만들어 heapq의 맨 앞으로 오게 해야함
        heapq.heappush(tmp, -jewels[0][1])
        # 중요 - 확인한 보석은 보석을 저장하고 있는 우선순위 큐에서 제거
            # 제거해야 다음 가방에서 확인해야할 보석의 개수가 줄어들으므로 시간초과를 방지할 수 있음
        heapq.heappop(jewels)

    # 가방 수만큼 for문 반복할때마다 하나씩 보석의 가치를 더해주는 것이므로 가방수 하나당 보석 한개가 보장됨
    if tmp:
        # tmp는 항상 가치가 높은 보석이 맨앞에 있는 것을 보장하기 때문에 heap에서 pop하면 가장 가치가 높은 보석을 answer에 더할 수 있음
        # 중요, 주의 : -(마이너스)를 하는 이유는 heapq에 가치값을 넣을 때 min_heap 문제로 -형태로 가치가 저장되었기 때문에 -(가치값(음수 형태))하면 양수가 되기 때문
        answer -= heapq.heappop(tmp)

print(answer)
#==============================================================================
# 내 코드 - 시간초과
    # 보석개수와 가방개수의 입력범위가 크기 때문에
    # 매번 반복할때마다 보석개수이든 가방개수이든 확인해야하는 원소의 개수를 줄여야하는데 그렇지 못한 코드이기 때문에 시간초과가 발생된것으로 추정
#==============================================================================
import sys
from collections import deque

answer = 0
# 보석 개수, 가방 개수 입력
n, k = map(int, sys.stdin.readline().split())
# 보석 무게, 보석 가격 입력
jewels = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 가방에 담을 수 있는 최대 무게 입력
bags = [int(sys.stdin.readline()) for _ in range(k)]

# 보석을 보석 가격 기준으로 내림차순 정렬
jewels.sort(key = lambda x : (-x[1], -x[0]))

queue = deque()
for j in jewels:
    queue.append(j)
# 가방 무게기준으로 오름차순 정렬
bags.sort()

# 가방 사용했는지 여부 리스트
bag_used = [0] * k

# 보석이 없을때까지 반복하면서
while queue:
    # 보석을 queue에서 꺼내기
    weight, value = queue.popleft()
    # 가방을 반복하면서
    for i in range(k):
        # 만약 아직 사용안한 가방(0)이라면
        if bag_used[i] == 0:
            # 만약 보석의 무게가 가방이 수용하는 무게보다 적거나 같다면
            if weight <= bags[i]:
                # answer에 보석 가격 추가
                answer += value
                # 가방 사용 여부 리스트에 사용 표시
                bag_used[i] = 1
                # break
                break

# answer 출력
print(answer)