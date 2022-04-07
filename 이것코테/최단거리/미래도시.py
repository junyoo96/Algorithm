INF = int(1e9)

# 입력받기 
# n : 전체 회사의 개수 
# m : 전체 경로의 개수 
n, m = map(int, input.split())
# x : 물건 판매 회사 노드 번녿(최종 목적지 노드)
# k : 소개팅 회사 번호 (거쳐갈 노드)
x, k = map(int, input.split())

# 그래프 초기화 
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화 
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
        graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화 
for _ in range(m):
  a, b = map(int, input.split())
  graph[a][b] = 1
  graph[b][a] = 1

# 점화식에 따라 플로이드 위셜 알고리즘 수행 
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      # 점화식 
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출발노드 1부터 노드 k를 거쳐서 노드 x 까지 가는 최단거리 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1 출력
if distance >= INF:
  print("-1")
# 도달할 수 있다면, 최단 거리 출력 
else:
  print(distance)
