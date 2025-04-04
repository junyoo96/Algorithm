# 10:18~45 / 10:50~
# 12:11~12:33/12:33~12:43
# 9:45~10:07/10:07~10:45

# n : 그림 크기
#     R , G ,B 색깔
#     구역은 같은 색으로 이루어짐
#         같은 색상이 상하좌우로 인접한 경우 같은 구역
#         빨간색과 초록색이 인접해 있는 경우도 같은 색상
# answer : 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수 구하기
#====================================================================
# 최적화 코드
import sys
sys.setrecursionlimit(100000)

n = int(input())
# 중요 - 사전에 색약용 맵을 따로 만들어 R과 G 동일하게 저장하기
# 색약아닌 사람 맵이자 방문 여부 저장
normal = [[0] * n for _ in range(n)]
# 색약용 사람 맵이자 방문 여부 저장
redgreen = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(n):
        normal[i][j] = tmp[j]
        redgreen[i][j] = tmp[j]
        # 색약용 맵에는 R과 G 동일한값으로 저장
        if tmp[j] == 'G':
            redgreen[i][j] = 'R'

# 방향 그래프
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, arr):
    current_color = arr[x][y]
    arr[x][y] = 0

    # 상하좌우 방향을 반복하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 만약 이동할 좌표가 범위안에 있고 이동할 좌표를 방문한적이 없고 현재좌표의 색과 이동할 좌표의 색이 같다면
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and current_color == arr[nx][ny]:
            dfs(nx, ny, arr)

# 적록색약 아닌 경우 카운트
normal_count = 0
# 적록색약인 경우 카운트
redgreen_count = 0
for i in range(n):
    for j in range(n):
        if normal[i][j] != 0:
            dfs(i, j, normal)
            normal_count += 1
        if redgreen[i][j] != 0:
            dfs(i, j, redgreen)
            redgreen_count += 1

print(normal_count, redgreen_count)
# ===================================================================
# 내 코드
import sys
sys.setrecursionlimit(100000)

# n 입력
n = int(sys.stdin.readline())
# 그림 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline()))

# 상우하좌 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 색약인 경우 방문 여부 그래프
redgreen_visited = [[0] * n for _ in range(n)]
# 색약아닌 경우 방문 여부 그래프
normal_visited = [[0] * n for _ in range(n)]

# 적록색약 사람의 경우 구역수 변수
redgreen = 0
# 적록색약 아닌 사람 경우 구역수 변수
normal = 0

# 함수 dfs(방문 좌표, 방문 여부 그래프, 현재 색, 색약여부)
def dfs(x, y, visited, color, is_red_green):
    # 상우하좌를 반복하면서
    for i in range(4):
        # 이동할 좌표 계산
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 이동할 좌표가 올바른 범위 안에 있고 아직 방문하지 않았다면
        if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] == 0:
            # 이동할 좌표의 색이 현재 색과 동일하다면
            if graph[nx][ny] == color:
                # 해당 좌표 방문처리
                visited[nx][ny] = 1
                dfs(nx, ny, visited, color, is_red_green)
            # 동일하지 않다면
            else:
                # 만약 색약이고 현재 좌표의 색과 이동할 좌표의 색이 파랑이 아니라면
                if is_red_green and graph[x][y] != "B" and graph[nx][ny] != "B":
                    # 해당 좌표 방문처리
                    visited[nx][ny] = 1
                    dfs(nx, ny, visited, graph[nx][ny], is_red_green)

# 그림 그래프를 반복하면서
for i in range(n):
    for j in range(n):
        # 색약의 경우
        # 만약 방문할 좌표가 올바른 범위 안에 있고 아직 방문하지 않았다면
        if redgreen_visited[i][j] == 0:
            # 해당 좌표 색약인 경우 방문여부 그래프에서 방문처리(1)
            redgreen_visited[i][j] = 1
            # 적록색약 구역수 1 증가
            redgreen += 1
            # dfs 함수 호출(방문 좌표, 방문 여부 그래프, 현재 색, 색약여부(True))
            dfs(i, j, redgreen_visited, graph[i][j], True)

        # 색약아닌 경우
        # 만약 방문할 좌표가 올바른 범위 안에 있고 아직 방문하지 않았다면
        if normal_visited[i][j] == 0:
            # 해당 좌표 색약아닌 경우 방문여부 그래프에서 방문처리(1)
            normal_visited[i][j] = 1
            # 적록색약 아닌 사람 구역수 1 증가
            normal += 1
            # dfs 함수 호출(방문 좌표, 방문 여부 그래프, 현재 색, 색약여부(False))
            dfs(i, j, normal_visited, graph[i][j], False)

# answer 출력
print(normal, redgreen)