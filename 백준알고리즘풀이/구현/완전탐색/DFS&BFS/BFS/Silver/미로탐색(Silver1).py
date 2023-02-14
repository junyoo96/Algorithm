# 9:44~9:54 / 9:55~10:10 (26분)

# n, m : 행,열
    # 1 : 이동가능칸
    # 0 : 이동불가능칸
# 상우하좌로 이동가능
# answer : 1,1에서 출발하여 n, m까지 지나야 하는 최소 칸 수
    # 칸에는 시작위치와 도착위치도 포함
#=============================================================
from collections import deque

# n, m 입력
n, m = map(int, input().split())
# 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상우하좌 그래프
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# deque에 (시작 위치) 추가
queue = deque([(0, 0)])

# queue를 반복하면서 - while
while queue:
    # queue에서 현재 좌표 꺼내기
    x, y = queue.popleft()
    # 상우하좌를 반복하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 올바른 범위 안에 있다면
        if 0 <= nx < n and 0 <= ny < m:
            # 만약 방문할 좌표의 칸이 이동가능한 칸이라면
            if graph[nx][ny] == 1:
                # queue에 (방문할 좌표) 추가
                queue.append((nx, ny))
                # 방문할 좌표에 현재 좌표의 값 + 1 저장
                graph[nx][ny] = graph[x][y] + 1

# answer 출력
print(graph[n-1][m-1])


