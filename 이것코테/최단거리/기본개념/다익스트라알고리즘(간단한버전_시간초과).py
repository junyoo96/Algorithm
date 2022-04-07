import sys
input = sys.stdin.readline # input()보다 더 빠르게 동작하는 방법
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# n : 노드의 개수 , m : 간선(에지)의 개수
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기 
start = int(input())
# graph =  각 노드에 연결되어 있는 노드에 대한 정보를 담는 2차원 리스트
graph = [[] for i in range(n+1)]
# visited : 노드를 방문한 했는지 여부 체크 리스트 
visited = [False] * (n+1)
# distance : 최단 거리 테이블
  # 최단 거리 테이블을 모두 무한으로 초기화 
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기 
for _ in range(m):
  a, b, c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용(거리)이 c라는 의미
  graph[a].apppend((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드(graph에서의 노드의 인덱스)
  for i in range(1, n+1):
    # 현재까지의 최단 거리보다 거리가 더 짧고, 아직 방문하지 않은 노드라면
    if distance[i] < min_value and not visited[i]:
      # 최단 거리 갱신
      min_value = distance[i]
      # 최단 거리 갱신한 노드의 인덱스 반환 
      index = i
  return index

# 다익스트라 알고리즘 
def dijkstra(start):
  # 시작 노드에 대해서 초기화 
  distance[start] = 0 
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복 
  for i in range(n-1):
    # now : 현재 방문한 노드 
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리 
    now = get_smallest_node()
    visited[now] = True
    # 현재 방문한 노드와 연결된 다른 노드들 확인
    for j in graph[now]:
      # 연결된 다른 노드들과 출발 노드 간의 거리 계산 
      cost = distance[now] + j[1]
      # 현재 방문한 노드를 거쳐서 연결된 다른 노드로 이동하는 거리가 더 짧은 경우 
      if cost < distance[j[0]]:
        # 최단 거리 테이블 갱신 
        distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력 
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print("INFINITY")
  # 도달할 수 있는 경우 거리를 출력 
  else:
    print(distance[i])
