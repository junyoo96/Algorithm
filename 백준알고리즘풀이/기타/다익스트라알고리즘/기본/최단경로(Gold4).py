# 1:37~

# v : 정점개수(1~20,000)
# e : 간선개수(1~300,000)
# w : 가중치(1~10)
# answer : 주어진 시작점에서 다른 모든 정점까지의 최단 경로 출력
# 시작점 자신은 0으로 출력
# 경로가 존재하지 않는 경우 INF로 출력
# =====================
import heapq
import sys

input = sys.stdin.readline

# INF 정의
INF = int(1e9)
# v, e 입력
V, E = map(int, input().split())
# 시작정점 입력
K = int(input())
# 간선개수만큼 반복하면서 그래프 입력
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # u(시작),v(끝),w(가중치) 입력
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
# 거리저장 리스트
distances = [INF] * (V + 1)

# 다익스트라 함수
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        distance, current = heapq.heappop(queue)
        if distances[current] < distance:
            continue

        for next_idx, next_distance in graph[current]:
            if distance + next_distance < distances[next_idx]:
                heapq.heappush(queue, (distance + next_distance, next_idx))
                distances[next_idx] = distance + next_distance


# 다익스트라 함수 호출
dijkstra(K)

# 거리저장 리스트를 반복하면서
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
        continue

    print(distances[i])