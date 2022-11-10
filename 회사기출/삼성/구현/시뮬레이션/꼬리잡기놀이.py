# 12:00~ / 실패(2시간 사용, 아이디어 발상 실패)

# n : 격자 크기
# m : 팀 개수
# k : 라운드 수
# 3명이상 한팀
    # 머리사람, 나머지, 꼬리사람
    # 각 팀은 주어진 이동선 따라서만 이동
# 이동선은 끝이 이어져있음
    # 이동선은 서로 겹치지 않음
    # 이동선 각 칸은 반드시 2개의 인접한 칸만 존재
    # 하나의 이동선에는 하나의 팀만 존재

# 게임
# 라운드별로 진행
    # 1. 각 팀은 머리사람 따라서 한칸 이동
    # 2. 각 라운드마다 공이 정해진 선을 따라 던져짐
        # 4n번째 라운드 넘어가는 경우에는 다시 1번째 라운드의 방향으로 돌아감
        # 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게 되는 사람이 공을 얻게 되어 점수를 얻음
            # 점수 : 머리사람을 시작으로 팀내에서 k번째 사람이라면, k의 제곱만큼 점수 얻음
                # 아무도 공 못받으면 아무 점수도 획득 못함
    # 3. 공을 획득한 팀은 머리사람과 꼬리사람이 바뀜(진행 방향이 바뀜)

# 빈칸(0), 머리사람(1), 나머지(2), 꼬리사람(3), 이동선(4)
# ==================================================

# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
# 격자 입력
board = [[0] * (n + 1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

# 각 팀별 레일(이동선) 좌표 관리
    # 알고리즘에 따라 (머리사람 -> 나머지 -> 꼬리사람 -> 이동선) 순으로 들어감
    # 이후에도 (머리사람 -> 나머지 -> 꼬리사람 -> 이동선)은 보장됨
v = [[] for _ in range(m + 1)]
# 각 팀별 꼬리사람이 그 팀에서 몇번째 index에 있는지 관리
tail = [0] * (m + 1)
visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

# 격자 내 레일에 각 팀 번호를 적는 변수
board_idx = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

ans = 0

dxs = [-1,  0, 1, 0]
dys = [ 0, -1, 0, 1]


def is_out_range(x, y):
    # 현재 격자의 맨 왼쪽위가 1,1 부터 좌표가 시작
    return not (1 <= x and x <= n and 1 <= y and y <= n)


# 초기 레일(이동선)을 만들기 위해 dfs를 이용
# idx : 현재 팀번호
def dfs(x, y, idx):
    # 방문 처리
    visited[x][y] = True
    # 레일칸에 팀번호 적기
    board_idx[x][y] = idx
    # 상하좌우를 반복하면서
    for dx, dy in zip(dxs, dys):
        # 이동할 좌표 계산
        nx, ny = x + dx, y + dy
        # 만약 이동할 좌표가 격자 범위를 벗어났다면
        if is_out_range(nx, ny):
            continue

        # 만약 이미 지나간 레일이거나 레일이 아니라면
        if board[nx][ny] == 0:
            continue
        # 만약 이미 방문했다면 넘어가기
        if visited[nx][ny]:
            continue

        # 가장 처음 탐색할 때(해당 팀에 좌표가 1개 밖에 없는경우) 머리사람(1)에서 꼬리사람(3)이 있는 방향으로 dfs를 진행
            # 나머지(2)인 방향으로 가야 머리사람에서 꼬리사람으로 이어지는 방향으로 이동하기 때문
        if len(v[idx]) == 1 and board[nx][ny] != 2:
            continue

        # 해당 팀의 레일 좌표 리스트에 이동할 좌표 추가
        v[idx].append((nx, ny))
        # 만약 이동할 좌표에 있는게 꼬리사람이라면
        if board[nx][ny] == 3:
            # 꼬리사람 리스트의 현재 팀에 현재 팀의 인원수 저장
            tail[idx] = len(v[idx])
        # dfs(이동할 좌표, 현재팀번호)
        dfs(nx, ny, idx)

# 초기 작업 함수
# 각 팀별로 레일 좌표 저장
def init():
    # 팀 개수 변수
    cnt = 1

    # 레일을 각 팀별로 머리사람의 좌표만 저장
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 만약 머리사람이라면
            if board[i][j] == 1:
                v[cnt].append((i, j))
                # 팀 개수 증가
                cnt += 1

    # 각 팀별로 머리사람 좌표를 반복하면서, dfs를 통해 팀별로 레일을 벡터에 순서대로 넣기
    for i in range(1, m + 1):
        # 해당 팀의 머리사람 좌표 불러오기
        x, y = v[i][0]
        dfs(x, y, i)

# 중요 - 각 팀을 이동시키는 함수
def move_all():
    # 1. 각 팀마다 머리사람 방향으로 한칸씩 이동
    # 팀 개수만큼 반복하면서
    for i in range(1, m + 1):
        # 각 팀에 대해 레일을 한 칸씩 뒤로(머리사람-> 이동선 방향) 이동
        # 저장된 레일 중 가장 마지막 레일
        tmp = v[i][-1]
        # 레일 좌표를 뒤에서부터 반복하면서
        for j in range(len(v[i]) - 1, 0, -1):
            # 레일을 한칸씩 뒤로 이동
            v[i][j] = v[i][j - 1]
        # 제일 뒤에 있던 레일 좌표는 맨 앞 좌표로 이동
        v[i][0] = tmp

    # 2. 사람들이 이동했으므로 보드의 정보도 갱신
    # 팀 개수 만큼 반복하면서
    for i in range(1, m + 1):
        # 벡터에 저장한 정보를 바탕으로 보드의 표기 역시 바꾸기
        # j : 팀내의 팀원 현재 좌표 index
        # (x, y) : 팀내의 팀원 현재 좌표
        for j, (x, y) in enumerate(v[i]):
            # (머리사람 -> 나머지 -> 꼬리사람 -> 이동선)이 보장되기 때문에 밑에 if문으로 처리가능한 것
            # 만약 현재 index가 머리사람이라면
            if j == 0:
                # 보드에서 머리사람으로 표시
                board[x][y] = 1
            # elif 현재 index가 꼬리사람의 index보다 작다면
            elif j < tail[i] - 1:
                # 보드에서 나머지로 표시
                board[x][y] = 2
            # elif 현재 index가 꼬리사람의 index라면
            elif j == tail[i] - 1:
                # 보드에서 꼬리사람으로 표시
                board[x][y] = 3
            else:
                # 보드에서 이동선으로 표시
                board[x][y] = 4

# (x, y) 지점에 공이 닿았을 때의 점수를 계산합니다.
def get_point(x, y):
    global ans
    # 공이 닿은 사람의 팀 번호
    idx = board_idx[x][y]
    # 공이 닿은 사람이 팀에서 몇번째 사람인지 확인
    cnt = v[idx].index((x, y))
    # 점수 계산
    ans += (cnt + 1) * (cnt + 1)

# turn 번째 라운드의 공을 던짐
# 공을 던졌을 때 이를 받은 팀의 번호를 반환
def throw_ball(turn):
    # n 7 , turn 1, k 1 -> t : 1
    # n 7,  turn 8, k 1 -> t : 8
    # + 1 하는 이유는 board의 크기가 n + 1이기 때문
    t = (turn - 1) % (4 * n) + 1

    # 만약 1~n 라운드라면
    if t <= n:
        # 왼쪽에서 오른쪽 방향으로 공을 던집니다.
        for i in range(1, n + 1):
            # 사람이 있는 첫번째 좌표 찾기(1~3은 사람에 해당하는 표시)
            if 1 <= board[t][i] and board[t][i] <= 3:
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장
                get_point(t, i)
                # 맞은 팀의 번호를 반환
                return board_idx[t][i]
    # elif n+1 ~ 2*n 라운드라면
    elif t <= 2 * n:
        # 아래에서 윗쪽 방향으로 공을 던짐
        t -= n # t를 1~n 사이 값으로 맞춰주기 위해
        for i in range(1, n + 1):
            # 사람이 있는 첫번째 좌표 찾기(1~3은 사람에 해당하는 표시)
            if 1 <= board[n + 1 - i][t] and board[n + 1 - i][t] <= 3:
                get_point(n + 1 - i, t)
                return board_idx[n + 1 - i][t]
    # elif 2n+1 ~ 3n 라운드의 경우
    elif t <= 3 * n:
        # 오른쪽에서 왼쪽 방향으로 공을 던짐
        t -= (2 * n) # t를 1~n 사이 값으로 맞춰주기 위해
        for i in range(1, n + 1):
            # 사람이 있는 첫번째 좌표 찾기(1~3은 사람에 해당하는 표시)
            if 1 <= board[n + 1 - t][n + 1 - i] and board[n + 1 - t][n + 1 - i] <= 3:
                get_point(n + 1 - t, n + 1 - i)
                return board_idx[n + 1 - t][n + 1 - i]
    # elif 3n+1 ~ 4n 라운드의 경우
    else:
        # 위에서 아랫쪽 방향으로 공을 던짐
        t -= (3 * n) # t를 1~n 사이 값으로 맞춰주기 위해
        for i in range(1, n + 1):
            # 사람이 있는 첫번째 좌표 찾기(1~3은 사람에 해당하는 표시)
            if 1 <= board[i][n + 1 - t] and board[i][n + 1 - t] <= 3:
                get_point(i, n + 1 - t)
                return board_idx[i][n + 1 - t]

    # 공이 그대로 지나간다면 0을 반환
    return 0

# 공을 획득한 팀을 순서를 바꾸기(머리사람 -> 꼬리사람, 꼬리사람 -> 머리사람)
def reverse(got_ball_idx):
    # 아무도 공을 받지 못했으면 넘어가기
    if got_ball_idx == 0:
        return

    idx = got_ball_idx

    new_v = []

    # 중요 - 순서를 맞춰 new_v에 레일을 넣기
    # 중요 - 해당 팀에서 꼬리사람좌표부터 머리사람좌표까지 넣기
    for j in range(tail[idx] - 1, -1, -1):
        new_v.append(v[idx][j])

    # 중요 - 해당 팀에 나머지에 해당하는 좌표들에 대해 넣기
    for j in range(len(v[idx]) - 1, tail[idx] - 1, -1):
        new_v.append(v[idx][j])

    # 해당 팀의 레일 좌표 갱신
    v[idx] = new_v[:]

    # 팀원들의 변경된 좌표에 대해 보드의 표기 바꾸기
    for j, (x, y) in enumerate(v[idx]):
        # 만약 머리사람이라면
        if j == 0:
            board[x][y] = 1
        # elif 나머지라면
        elif j < tail[idx] - 1:
            board[x][y] = 2
        # elif 꼬리시람이라면
        elif j == tail[idx] - 1:
            board[x][y] = 3
        # else(이동선이라면)
        else:
            board[x][y] = 4


# 입력을 받고 구현을 위한 기본적인 처리 진행
init()
# 라운드수 만큼 반복하면서
for i in range(1, k + 1):
    # 각 팀을 머리사람을 따라 한칸씩 이동
    move_all()

    # i번째 라운드의 공을 던짐
    # 공을 쏴서 공을 받은 사람을 찾아 점수를 추가하고 팀 번호 반환
    got_ball_idx = throw_ball(i)

    # 공을 획득한 팀의 방향을 바꿈
    reverse(got_ball_idx)

print(ans)