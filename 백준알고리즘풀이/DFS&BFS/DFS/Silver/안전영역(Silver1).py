# 9:27~9:40 / 9:41~

# 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
# n : 행열 크기
# 각 원소는 지점의 높이를 표시
# answer : 물에 잠기지 않는 안정한 영역의 최대 개수
#=================================================================
# 내가 작성한 코드(2004ms)
#=================================================================
import sys
sys.setrecursionlimit(100000) # 주의 - 파이썬에서는 1000번이상의 recursion 발생하면 recursion error가 발생하므로, recursion 제한을 더 늘려서 설정
import copy

answer = 0 # 최대 안전영역 개수 계산
n = int(input()) # 행열 크기 입력
max_height = 1 # 가장 높은 지역 저장 변수

graph = [] # 그래프 입력
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        max_height = max(max_height, graph[i][j])

# 상우하좌 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 함수 - dfs(방문한 좌표, 그래프)
def dfs(x, y, height):
    # 만약 방문한 좌표가 올바른 범위안에 있으면
    if 0 <= x < n and 0 <= y < n:
        # 방문한 좌표를 아직 방문하지 않았거나(!=1) 비에 잠기는 않는 지역이라면
        if graph_copy[x][y] > height:
            # 방문처리(-1)
            graph_copy[x][y] = -1
            # 상우하좌를 반복하면서
            for i in range(4):
                # dfs 함수 호출(방문할 좌표에 이동한 좌표, 그래프)
                dfs(x + dx[i], y + dy[i], height)
            return True

    return False

# 높이를 반복하면서
for height in range(max_height): # 주의 - 문제에서 아무 지역도 물에 잠기지 않을 수 있다는 단서가 있으므로, 비가 아예 오지 않는 경우가 포함해야함
    safe = 0 # 안전영역
    graph_copy = copy.deepcopy(graph)
    # 그래프를 반복하면서
    for i in range(n):
        for j in range(n):
            # 만약 dfs 함수(방문한 좌표, 그래프)가 True이면
            if dfs(i, j, height):
                # 안전영역 증가
                safe += 1

    # 최대 안전영역 개수 계산
    answer = max(answer, safe)

# answer 출력
print(answer)

#==========================================================
# 개선한 코드(시간 단축, 1476ms)
#==========================================================
import sys
sys.setrecursionlimit(100000) # 주의 - 파이썬에서는 1000번이상의 recursion 발생하면 recursion error가 발생하므로, recursion 제한을 더 늘려서 설정
import copy

# answer 변수
answer = 0
# n 입력
n = int(input())
# 그래프 입력
max_height = 1
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        max_height = max(max_height, graph[i][j])

# 상우하좌 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 함수 dfs(방문한 좌표, 그래프)
def dfs(x, y, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 만약 방문한 좌표가 올바른 범위안에 있으면
        if 0 <= nx < n and 0 <= ny < n:
            # 비에 잠기지 높이보다 높고 아직 방문하지 않았다면
            if graph[nx][ny] > height and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(nx, ny, height)

# 높이를 반복하면서
for height in range(max_height): # 주의 - 문제에서 아무 지역도 물에 잠기지 않을 수 있다는 단서가 있으므로, 비가 아예 오지 않는 경우가 포함해야함
    safe = 0
    visit = [[0] * n for _ in range(n)] # 방문 여부 확인 그래프
    # 그래프를 반복하면서
    for i in range(n):
        for j in range(n):
            # 비에 잠기는 높이보다 높고 아직 방문하지 않았다면
            # 내 코드와 다르게 dfs 호출하기 전에 비에 잠기는 높이인지와 방문 여부를 확인
            if graph[i][j] > height and visit[i][j] == 0:
                # 방문처리
                visit[i][j] = 1
                # 안전영역 개수 증가
                safe += 1
                # dfs 호출
                dfs(i, j, height)

    # 최대 안전영역 개수 계산
    answer = max(answer, safe)

# answer 출력
print(answer)