n, m = map(int, input().split()) # n : 세로(행) , m : 가로(열)
data = [] # 원본 지도 
temp = [[0] * m for _ in range(n)] # 임시 지도 

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향(상, 우, 하, 좌)에 대한 리스트
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

# 안전 여역의 최대 크기 
result = 0

# dfs를 이용해 각 바이러스가 사방으로 퍼지도록 하기 
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 만약 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있다면
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      # 만약 빈칸이라면 
      if temp[nx][ny] == 0:
        # 해당 칸 바이러스로 갱신
        temp[nx][ny] = 2
        # 재귀 호출 
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하기
def get_score():
  score = 0 # 안전 영역

  # 빈칸인 경우만 안전 영역으로 계산 
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역 크기 계산
def dfs(count):
  global result
  # 3개의 벽이 모두 설치되었으면
  if count == 3:
    for i in range(n):
      for j in range(m):
        # 원본 지도로 임시 지도를 생성 
        temp[i][j] = data[i][j]

    # 만약 임시지도에서 바이러스이면 
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)

    # 안전 영역의 최댓값 계산 
    result = max(result, get_score())
    return 

  # 빈 공간에 벽 설치 (3가지 벽 조합을 할 때까지 차례대로 벽 선정)
  for i in range(n):
    for j in range(m):
      # 만약 빈칸이면
      if data[i][j] == 0:
        # 벽으로 갱신
        data[i][j] = 1
        # 벽 설치했으니 벽 증가 
        count += 1
        # dfs 시작 
        dfs(count)
        # 벽으로 갱신 했던 것 돌려놓기 
        data[i][j] = 0
        # 벽 돌려놓았으니 벽 감소
        count -= 1

dfs(0)
print(result)
