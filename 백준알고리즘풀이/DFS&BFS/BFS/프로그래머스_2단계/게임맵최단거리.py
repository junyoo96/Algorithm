# 11:23~11:34/11:34~11:47
# 캐릭터
# 이동 - 동서남북 한칸씩
# 1,1 위치에서 시작
# 벽 - 0(벽), 1(빈칸)
# answer : 캐릭터가 상대팀 진영에 도착하기 위해 지나가야 하는 칸의 개수 최소값
# 도착할 수 없을 때 -1
# ===============================================
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    # deque에 (시작위치, 이동한칸수) 추가
    queue = deque([0, 0, 1]) # 시작칸을 1칸으로 침
    # 현재 위치 방문처리(0으로)
    maps[0][0] = 0
    # 방향 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # while queue:
    while queue:
        # 현재위치, 이동한칸수 = deque에서 꺼내기
        x, y, move = queue.popleft()

        # 만약 현재위치가 n,m이라면
        if x == n - 1 and y == m - 1:
            answer = move
            break

        # 4가지 방향을 반복하면서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 이동할 위치로 갈 수 있고(0이 아니라면) 범위에서 벗어나지 않았다면
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0:
                    # deque에 (이동할 위치, 이동한칸수 + 1) 추가
                    queue.append([nx, ny, move + 1])
                    maps[nx][ny] = 0

    # 만약 answer가 0이라면(길 못찾았음)
    if answer == 0:
        # answer = -1
        answer = -1

    return answer