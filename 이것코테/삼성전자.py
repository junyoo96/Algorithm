#13:01~14:00
#14:00~

# n : 공간 크기 
  # 한 칸에는 최대 1마리 존재
# m : 물고기 수 
  # 아기상어 크기 2
    # 1초에 상하좌우로 인접한 한칸씩 이동 
    # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음 
    # 자신의 크기보다 작은 물고기만 먹을 수 있음 
    # 이동방식 
    # 먹을 수 있는 물고기가 공간에 없다면 아기상어는 엄마 상어에게 도움 요청 
    # 먹을 수 있는 물고기가 1마리라면, 물고기 먹으러감 
    # 1마리보다 많다면, 가장 가까운 물고기 먹으러감
      # 거리가 가장 가까운 물고기가 많다면, 가장 위에 있는 물고기
        # 여러 마리라면, 가장 왼쪽에 있는 물고기 먹기 
    # 거리는 아기상어에서 물고기 칸으로 이동하는 칸의 개수 최소값
    # 이동과 동시에 물고기 먹음   
    # 자신의 크기와 같은 수 물고기 먹을 때마다 크기 1 증가 

# answer : 아기 상어가 몇초 동안 엄마 상어에게 도움을 요청하지 않고 물고기 잡아먹을 수 있는지 구하기 

from collections import deque
INF = 1e9 # 무한을 의미하는 값으로 10억 설정 


answer = 0 # 현재까지 몇초 지났는지 시간 
n = int(input())
now_x = 0 # 아기 상어의 위치 
now_y = 0 # 아기 상어의 위치 
now_size = 2 # 아기 상어의 현재 크기
# 상우하좌 방향 리스트 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [] # 맵에 대한 정보
# 맵에 대한 정보 입력받기 
for i in range(n):
  tmp = list(map(int, input().split()))
  graph.append(tmp)
  # 아기 상어 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리 
  for j in range(n):
    if tmp[j] == 9:
      now_x = i
      now_y = j
      graph[i][j] = 0
  
# 모든 위치까지의 최단 거리만 계산하는 함수 
def bfs():
  # 값이 -1이리면 도달할 수 없다는 의미 
  dist = [[-1] * n for _ in range(n)] # 주의
  q = deque([(now_x, now_y)])
  # 시작 위치는 도달가능하기 때문에 0으로 설정 
  dist[now_x][now_y] = 0

  # q가 빌때까지 반복하면서 
  while q:
    x, y = q.popleft()
    # 상하좌우 4방향 확인 
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < n: 
        # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음 
        if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
          # 이동한 곳까지의 거리 갱신 
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))

  # 현재 아기상어 위치에서 모든 위치까지의 최단 거리 테이블 반환 
  return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기의 위치와 거기까지의 최단거리를 찾는 함수 
def find(dist):
  x, y = 0, 0
  min_dist = INF
  for i in range(n):
    for j in range(n):
      # 만약 도달이 가능하면서 먹을 수 있는 물고기인 경우
      if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < now_size:
        # 가장 가까운 물고기 1마리만 선택 
          # 문제에서 먹을 수 있는 물고기가 여러마리 있을 경우 맨위 그중에서 맨 왼쪽을 우선해서 먹으라고 했는데, dist 테이블을 돌면서 위와 그리고 왼쪽에서부터 확인하기 때문에 따로 체크안해도됨
        if dist[i][j] < min_dist:
          x, y = i, j
          min_dist = dist[i][j]

  # 먹을 수 있는 물고기가 없는 경우 
  if min_dist == INF: 
    return None
  # 먹을 수 있는 물고기가 있는 경우 
  else:
    # 먹을 물고기의 위치와 최단 거리 반환
    return x, y, min_dist

ate = 0 # 현재 크기에서 먹은 양 

while True:
  # 먹을 수 있는 물고기 위치와 최단 거리 찾기 
  value = find(bfs()) 
  # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력 
  if value == None:
    print(answer)
    break
  else:
    # 현재 위치 갱신 
    now_x, now_y = value[0], value[1]
    # 이동 거리 변경 
    answer += value[2]

    # 먹은 위치에는 아무것도 없도록 처리 
    graph[now_x][now_y] = 0
    # 먹은 양 증가
    ate += 1

    # 자신의 크기 이상으로 먹은 경우, 크기 증가 
    if ate >= now_size:
      now_size += 1
      ate = 0
    
    
