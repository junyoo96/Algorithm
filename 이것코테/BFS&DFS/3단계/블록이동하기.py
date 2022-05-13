# 11:25~ 11:58
# 12:00~
# n : 지도 크기 (5~100)
# 2x1 크기 로봇을 움직여 n,n 위치까지 이동할 수 있게
# 로봇이 차지하는 두칸 중 어느 한칸이라도 n,n 위치에 도착하면 됨
# 왼쪽 상단 좌표 1,1
# 0 : 빈칸, 1 : 벽
# 로봇 시작위치는 1,1 좌표에서 가로 방향 상태
# 로봇 움직이기
# 90도씩 회전 가능
# 어느 칸 이득 축 가능
# 회전하는 축 칸에서 대각선 방향 칸에는 벽이 없어야 함
# 이동하거나 회전하는데 걸리는 시간 1초

# return - n,n 위치까지 이동하는데 필요한 최소 시간

# 좌표 반복시 1부터 시작

from collections import deque

# 이동 가능한 위치들을 반환하는 함수
def get_next_pos(pos,board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합, 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 1. 상우하좌로 이동하는 경우에 대해 처리
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 2. 회전하는 경우에 대해 처리
    # 로봇이 수평으로 놓여있는 경우
    if pos1_x == pos2_x:
        # 위쪽으로 회전하거나, 아래쪽으로 회전
        for i in [-1, 1]:
            # 축이 pos1일때와 pos2일때 움직인 칸이 둘다 비어있는 경우
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 수직으로 놓여있는 경우
    elif pos1_y == pos2_y:
        # 왼쪽으로 회전하거나 오른쪽으로 회전
        for i in [-1, 1]:
            # 축이 pos1일때와 pos2일때 움직인 칸이 둘다 비어있는 경우
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치 반환
    return next_pos

def solution(board):
    n = len(board) # 지도 크기
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # BFS 수행
    q = deque()
    visited = []
    pos = {(1,1), (1,2)} # 로봇 시작 위치 설정
    # 큐에 현재 좌표 위치와 출발지부터의 거리를 저장
    q.append((pos, 0))
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n,n) 위치에 로봇이 도달했다면, 최단 거리이므로 변환
        if (n,n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0