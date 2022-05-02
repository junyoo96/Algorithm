#11:31~11:38
#11:38~
from collections import deque

#n : 도시 개수
#m : 도로 개수
#k : 거리 정보
#x : 출발도시번호
n, m, k, x = map(int, input().split())
# 그래프를 이차원 리스트로 구현
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력 받기 
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# 모든 도시에 대한 최단 거리 초기화 
distance = [-1] * (n + 1) 
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정 

# BFS(너비우선탐색) 수행 
queue = deque([x])
while queue:
  now = queue.popleft()
  # 현재 도시에 인접한 모든 도시를 확인 
  for next in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next] == -1:
      # 최단 거리 갱신
      distance[next] = distance[now] + 1
      queue.append(next)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력 
if check == False:
  print(-1)
