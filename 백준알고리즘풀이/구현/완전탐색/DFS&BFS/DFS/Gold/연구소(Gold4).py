# 10:30~11:00/11:00~11:12

# n, m : 연구소 크기
# 연구소
    # 빈칸 0, 벽 1, 바이러스 2
# 바이러스
    # 상하좌우로 인접한 빈칸으로 이동 가능
# 안전영역
    # 바이러스가 퍼질 수 없는 곳
# 세울 수있는 벽의 개수 무조건 3개
# answer : 안전영역의 최대 크기 출력
# ============================================
from itertools import combinations
import copy

# dfs로 바이러스 살포
def dfs(x, y, arr_):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    arr_[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr_[nx][ny] == 0:
            dfs(nx, ny, arr_)

n, m = map(int, input().split())
# 바이러스 좌표 입력
viruses = []
# 연구소 지도 입력
arr = []
# 벽 설치 가능한 좌표 입력
positions = []

# 바이러스와 벽 설치 가능 좌표 입력 받기
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        # 만약 빈칸이라면
        if arr[i][j] == 0:
            positions.append((i, j))
        # elif 바이러스라면
        elif arr[i][j] == 2:
            viruses.append((i, j))

# 안전영역 카운트
answer = 0
# 벽 후보를 반복하면서
for walls in combinations(positions, 3):
    arr_tmp = copy.deepcopy(arr) # 주의 - 깊은복사 사용법

    # 벽 설치
    for w_x, w_y in walls:
        arr_tmp[w_x][w_y] = 1

    # 바이러스 살포
    for v_x, v_y in viruses:
        dfs(v_x, v_y, arr_tmp)

    # 안전영역 카운트
    count = 0
    for i in range(n):
        count += arr_tmp[i].count(0)

    # 안전영역 최대 갱신
    answer = max(answer, count)

print(answer)