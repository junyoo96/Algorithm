# 11:12~11:33 / 11:34~11:53 (41분)

# n, m : 토마토 창고 크기(행, 열)
# 1 익은 토마토, 0 안 익은 토마토, -1 토마토가 들어있지 않은 칸
    # 보관 후 하루 지나면 익은 토마토에 상하좌우에 인접한 안 익은 토마도 익게됨
    # 상자 일부 칸에는 토마토가 들어있지 않을 수 있음

# answer : 토마토들이 며칠이 지나면 다 익는 최소 일수
    # 저장될 때부터 모든 토마토가 익어있다면 0 출력
    # 모두 익지 못하는 상황이면 - 1 출력
#=============================================================
from collections import deque
import sys

answer = 0
# m,n 입력
m, n = map(int, sys.stdin.readline().split())
# 익은 토마토 리스트
done_tomatoes = []
# 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    # 익은 토마토의 좌표는 리스트에 추가
    for j in range(m):
        if graph[i][j] == 1:
            done_tomatoes.append(((i, j), 0))

# 상우하좌 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 만약 모든 토마토가 이미 익어있다면
if len(done_tomatoes) == n * m:
    answer = 0
else:
    # deque에 (익은 토마토의 좌표, 현재 시간 0)를 추가
    queue = deque(done_tomatoes)
    # queue를 반복하면서 - while
    while queue:
        # queue에서 좌표 꺼내기
        pos, day = queue.popleft()
        x, y = pos
        # 상우하좌를 반복하면서
        for i in range(4):
            # 이동할 좌표 계산
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 이동할 좌표가 올바른 범위안에 있다면
            if 0 <= nx < n and 0 <= ny < m:
                # 만약 이동할 좌표의 값이 안익은 토마토 라면
                if graph[nx][ny] == 0:
                    # queue에 (이동할 좌표 값, 현재 시간 + 1) 넣기
                    queue.append(((nx, ny), day + 1))
                    # 이동할 좌표의 값을 방문처리(1)
                    graph[nx][ny] = 1
                    # answer와 현재시간 + 1 중 더 큰값으로 갱신
                    answer = max(answer, day + 1)

    # graph를 반복하면서 안익은 토마가 있다면
    for row in graph:
        if row.count(0) != 0:
            answer = -1

print(answer)

