import heapq # 우선순위 큐 사용(최소힙 기반)
import sys 

input = sys.stdin.readline
INF = int(1e9)

# n : 도시의 개수 
# m : 통로의 개수
# start : 메시지가 출발하는 도시 
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화 
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기 
for _ in range(m):
  # 특정도시 x에서 다른 특정도시 y로 이어지는 통로가있는데, 메시지가 전달되는 시간이 z라는 의미
  x, y, z = map(int, input().split())
  graph[x].append((y,z))

# 다익스트라 알고리즘 정의
def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.headpush(q,(0,start))
  distance[start] = 0 
  while q: # 우선순위 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기 
    dist, now = heapq.heapop(q)
    # 이미 처리된(방문한) 노드라면 
    if distance[now] < dist:
      continue # 넘어가기 

    # 현재 노드와 연결된 다른 인접한 노드들을 확인 
    for i in graph[now]:
      # i : (노드 번호, 1번 노드부터 이 노드까지의 거리 )
      cost = dist + i[1] # 거리 계산
      # 현재 계산한 거리가 최단 거리 테이블의 최단 거리보다 작다면
      if cost < distance[i[0]]:
        distance[i[0]] = cost # 최단 거리 테이블 갱신
        heapq.headpush(q, (cost, i[0])) #현재 노드와 연결되어있는 노드 우선순위큐에 삽입

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도시 개수 
count = 0
# 출발 도시 c로부터 가장 거리가 먼 도시의 거리 
max_distance = 0
for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

# -1 하는 이유는 출발 도시(시작 노드)는 도시 개수에서 제외해야 되기 때문 
print(count - 1, max_distance)
