import heapq # 최소 힙 방식의 우선순위 큐 라이브러리 
import sys 
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기 
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기 
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화 
distance = [INF] * (n+1)

# 그래프의 모든 간선 정보를 입력받기 
for _ in range(m):
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  # 우선순위 큐(heapq방식으로 사용할 예정)
  q = []
  # 시작 노드를 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입 
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q : # 우선순위 큐가 비어있지 않는동안 
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기(기존코드의 get_smallest_node 함수 대체 )
    dist, now = heapq.heapop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
     # 우선순위 큐에서 꺼낸 현재 방문 노드까지의 거리가 최단 거리 갱신 테이블에서의명시된 해당 노드까지의 거리보다 클 경우 갱신이 이미 됐다고 판단    
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 최단 거리 테이블에서 명시된 거리보다 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heaqpush(q,(cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한이라고출력 
  if distance[i] == INF:
    print("INFINITY")
  else:
      print(distance[i])
