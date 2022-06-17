#10:35~10:54
#10:54~
# n : 헛간의 개수
# m : 양방향 통로 개수
# 항상 어떤 헛간에서 다른 어떤 헛간으로 도달 가능
# answer : 1벗 헛간으로부터 최단 거리가 가장 먼 헛간의 번호, 헛간까지의 거리, 헛간과 같은 거리를 갖는 개수
    # 최단거리가 가장 먼 헛간 : 지나가야하는 길의 최소 개수가 가장 많은 목적지 헛간

# 값 갱신

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향으로 갈 수 있으니 양쪽다 입력
    graph[a].append((1, b))
    graph[b].append((1, a))

# 최단 거리 테이블
distance = [INF] * (n + 1) # 주의 - 1차원 리스트 여러개 원소로 초기화 방법
start = 1 # 시작 노드
# 시작 노드까지의 거리 설정
distance[start] = 0
q = [(0, start)] # heaqp에 비용,시작노드 넣기

# 다익스트라 알고리즘 시작
# heapq의 원소가 있을 동안
while q:
    # dist, now = heapq에서 최상위 원소 pop
    dist, now = heapq.heappop(q)
    # 만약 이미 방문했다면
    if distance[now] < dist:
        continue
    # 그래프에서 현재 노드에 연결된 노드를 반복하면서
    for d, idx in graph[now]:
        cost = dist + d
        # 만약 distance 테이블값보다 거리가 짧다면
        if cost < distance[idx]:
            # distance 테이블 갱신
            distance[idx] = cost
            # heapq에 비용과 노드인덱스 삽입
            heapq.heappush(q, (cost, idx))

max_distance = 0 # 1벗 헛간으로부터 최단 거리가 가장 먼 헛간까지의 거리
max_node = 0 # 1벗 헛간으로부터 최단 거리가 가장 먼 노드 인덱스
result = [] # 해당 헛간과 같은 거리를 갖는 헛간의 개수

# distance 테이블을 반복하면서
for i in range(1, n + 1):
    # 만약 현재 최단 거리보다 멀다면
    if max_distance < distance[i]:
        # 값 갱신
        max_distance = distance[i]
        max_node = i
        result = [max_node]
    # 만약 현재 최단 거리보다 같다면
    elif distance[i] == max_distance:
        result.append(i)

# 답 출력
print(max_node, max_distance, len(result))




