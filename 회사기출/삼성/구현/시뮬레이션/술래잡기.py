# 11:22~11:34~12:33 / 1:13~ 실패
# 10:15~10:33/10:33~ 실패

# n : 격자 크기
# 술래
    # 정중앙
# m : 도망자
    # 중앙에서 시작하지 않음
    # 이동
        # 상하
            # 항상 아래쪽을 보고 시작
        # 좌우
            # 항상 오른쪽을 보고 시작
# h : 나무
    # 나무와 도망자가 겹칠 수 있음
# 규칙
    # m명의 도망자가 먼저 동시에 움직임
        # 술래와의 거리가 3이하인 도망자만 움직임
            # 움직였을 때 격자를 벗어나지 않는 경우
                # 움직이려는 칸에 술래가 있으면 움직이지 않음
                # 술래가 있지않다면, 해당 칸으로 이동
            # 움직였을 때 격자 벗어나는 경우
                # 먼저 방향 반대로 틀음
                # 바라보는 방향으로 움직였을 때 움직이려는 칸에 술래가 없다면 이동
    # 그 다음 술래가 움직임
        # 위 방향으로 시작해서 달팽이 모양으로 움직임
        # 끝에 도착하면 그대로 반대로 중심으로 돌아감
        # 이동후의 위치가 만약 이동방향이 틀어지는 지점이라면 바로 방향을 틀어줌
        # 만약 이동했는데 양끝에 해당하는 위치(1행1열 또는 정중앙)에 도착했다면, 방향 바로 틀어줘야함
        # 이동 직후, 턴을 넘기기 전에 시야내에 있는 도망자를 잡음
            # 시야는 현재 바라보는 뱡향 기준으로 현재 칸 포함해 3칸
                # 만약 나무가 놓여있다면, 해당 칸에 도망자는 나무에 가려져 보이지 않음
            # 잡힌 도망자는 사라짐
            # 술래는 점수 얻음(t번째 턴 * 현재 턴에서 잡힌 도망자 수)

    # 위를 k번 반복함(도망자 1턴, 술래 1턴 합쳐서 1번)
# answer : k번에 걸쳐 술래잡기 진행하는 동안 술래가 얻게될 총 점수
# 유의
    # 좌표 입력 받을 때 -1 해주기
#=======================================================================================
# 코드트리 코드

# 변수 선언 및 입력
n, m, h, k = tuple(map(int, input().split()))

# 각 칸에 있는 도망자(도망자가 바라보고 있는 방향만) 저장
hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]
# 임시로 움직인 칸에 도망자가 바라보고 있는 방향만 저장
next_hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]
# 나무 위치 저장
tree = [
    [False] * n
    for _ in range(n)
]

# 정방향 기준으로
# 현재 위치에서 술래가 움직여야 할 방향을 관리합니다.
seeker_next_dir = [
    [0] * n
    for _ in range(n)
]
# 역방향 기준으로
# 현재 위치에서 술래가 움직여야 할 방향을 관리합니다.
seeker_rev_dir = [
    [0] * n
    for _ in range(n)
]

# 술래의 현재 위치를 나타냄
seeker_pos = (n // 2, n // 2)
# 술래가 움직이는 방향이 정방향이면 True / 아니라면 False
forward_facing = True

# 술래가 얻을 수 있는 총 점수
answer = 0

# 술래 정보를 입력받습니다.
for _ in range(m):
    x, y, d = tuple(map(int, input().split()))
    hiders[x - 1][y - 1].append(d)

# 나무 정보를 입력받습니다.
for _ in range(h):
    x, y = tuple(map(int, input().split()))
    tree[x - 1][y - 1] = True

# 중요, 주의 - 술래가 움직일 방향 미리 전부 계산
# 정방향 시, 정중앙으로부터 끝(0,0)까지 각 칸에서 움직여야될 방향과
# 역방향 시, 끝(0,0)으로부터 정중앙까지 각 칸에서 움직여야될 방향 계산
def initialize_seeker_path():
    # 상우하좌 리스트
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 시작 위치와 방향,
    # 해당 방향으로 이동할 횟수를 설정합니다.
    curr_x, curr_y = n // 2, n // 2
    # move_dir = 움직일 방향
    # move_num = 움직일 칸 수
    move_dir, move_num = 0, 1

    # 현재 좌표가 둘다 0,0이 될때까지 반복하면서
    while curr_x or curr_y:
        # 움직일 칸 수 만큼 이동하면서
        for _ in range(move_num):
            # 정방향으로 움직일 때 현재칸에서 어떤 방향으로 이동할지 저장
            seeker_next_dir[curr_x][curr_y] = move_dir
            # 현재 좌표 이동
            curr_x, curr_y = curr_x + dx[move_dir], curr_y + dy[move_dir]
            # 역방향으로 움직일 때 현재칸에서 어떤 방향으로 이동할지 저장
            seeker_rev_dir[curr_x][curr_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # 이동하는 도중 (0, 0)으로 오게 되면, 움직이는 것을 종료
            if not curr_x and not curr_y:
                break

        # 방향을 바꿈(시계방향으로 방향 바꿈)
        move_dir = (move_dir + 1) % 4
        # 중요 - 만약 현재 방향이 위 혹은 아래가 된 경우에는 특정 방향으로 움직여야 할 횟수를 1 증가시킴(나선형으로 2차원배열에서 이동할 때 위또는 아래가 되면 움직여야할 횟수가 증가됨)
        if move_dir == 0 or move_dir == 2:
            move_num += 1

# 격자 내에 있는지를 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 도망자 이동 함수
def hider_move(x, y, move_dir):
    # 중요 - 좌우하상 리스트
    dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]

    nx, ny = x + dx[move_dir], y + dy[move_dir]

    # 만약 격자를 벗어난다면 우선 방향을 틀어줌
    if not in_range(nx, ny):
        # 중요 - 0이면 1, 1이면 0, 2이면 3, 3이면 2가 되게함
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        # 이동할 위치 계산
        nx, ny = x + dx[move_dir], y + dy[move_dir]

    # 이동할 위치에 술래가 없다면 이동
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    # 술래가 있다면 이동 안함
    else:
        next_hiders[x][y].append(move_dir)

# 도망자와 술래의 거리 계산
def dist_from_seeker(x, y):
    # 현재 술래의 위치를 불러옴
    seeker_x, seeker_y = seeker_pos
    # 거리 계산
    return abs(seeker_x - x) + abs(seeker_y - y)


def hider_move_all():
    # next hider를 초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    # 도망자를 전부 움직임
    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3 이내인 도망자들에 대해서만 이동
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            # 그렇지 않다면 현재 위치 그대로 넣어줌
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    # 도망자 위치 정보 갱신
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]

# 현재 술래가 바라보는 방향을 가져옴
def get_seeker_dir():
    # 현재 술래의 위치를 불러옴
    x, y = seeker_pos

    # 사전에 계산해놓은 어느 방향으로 움직여야 하는지에 대한 정보를 가져옴
    move_dir = 0
    if forward_facing: # 정방향이라면
        move_dir = seeker_next_dir[x][y]
    else: # 역뱡향이라면
        move_dir = seeker_rev_dir[x][y]

    return move_dir


def check_facing():
    global forward_facing

    # 정방향으로 끝(정방향 끝은 (0,0))에 다다른 경우라면, 방향을 바꾸기
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False
    # 역방향으로 끝(역방향 끝은 정중앙)에 다다른 경우여도, 방향을 바꾸기
    if seeker_pos == (n // 2, n // 2) and not forward_facing:
        forward_facing = True

# 술래 이동 함수
def seeker_move():
    global seeker_pos

    # 술래 좌표 불러옴
    x, y = seeker_pos
    # 상우하좌 리스트
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 현재 술래가 바라보는 방향을 가져옴
    move_dir = get_seeker_dir()
    # 가져온 방향으로 술래를 한 칸 이동
    seeker_pos = (x + dx[move_dir], y + dy[move_dir])
    # 주의 - 끝에 도달했는지 체크하고 도달했다면 방향을 바꿔주기
    check_facing()

def get_score(t):
    global answer

    # 상우하좌 리스트
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 현재 술래의 위치 불러옴
    x, y = seeker_pos
    # 술래의 방향을 불러옴
    move_dir = get_seeker_dir()

    # 시야 3칸을 바라봄
    for dist in range(3):
        nx, ny = x + dist * dx[move_dir], y + dist * dy[move_dir]

        # 격자를 벗어나지 않으며, 나무가 없는 위치라면 도망자들을 전부 잡음
        if in_range(nx, ny) and not tree[nx][ny]:
            # 해당 위치의 도망자 수 만큼 점수를 얻게됨
            # 주의 - 격자 한칸에 도망자들이 여러명 있을 수 있음
            answer += t * len(hiders[nx][ny])
            # 도망자들이 사라지게 됨
            hiders[nx][ny] = []

def simulate(t):
    print()

    # 도망자가 이동
    hider_move_all()
    # 술래 이동
    seeker_move()
    # 술래가 점수 얻기
    get_score(t)

# 중요 - 술래잡기 시작 전에 구현상의 편의를 위해 술래가 이동한 방향 정보를 미리 계산
initialize_seeker_path()

# for ss in seeker_next_dir:
#     print(*ss)
# print("==============")
# for ss in seeker_rev_dir:
#     print(*ss)
# print("==============")
# k번에 걸쳐 술래잡기를 진행
for t in range(1, k + 1):
    for hider in hiders:
        print(str(t) + "턴", hider)
    print("점수", answer, "뱡향", forward_facing, "술래", seeker_pos[0], seeker_pos[1], get_seeker_dir())
    print("=====================")
    simulate(t)

print(answer)
#=======================================================================================
# 내 코드
# 10:15~10:33

# n : 격자 크기
# 술래
    # 처음에 정중앙 위치
    #
# 도망자 m
    # 처음에 지정된 곳에 서있음(중앙에 없음)
    # 2가지 유형
        # 좌우 움직이는 유형
            # 항상 오른쪽 보고 시작
        # 상하 움직이는 유형
            # 항상 아래쪽 보고 시작
# 나무 h
    # 나무와 도망자가 초기에 겹쳐져 주어질 수 있음
# 술래잡기 게임
    # 도망자들이 움직임
        # 술래와의 거리가 3이하인 도망자만 움직임
            # 거리 = abs(x1-x2) + abs(y1-y2)
            # 만약 현재 바라보고 있는 방향으로 1칸 움직였을 때 격자를 벗어나지 않는다면
                # 만약 움직이려는 칸에 술래가 있다면 움직이지 않음
                # 만약 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동(나무가 있어도 괜찮음)
            # 만약 현재 바라보고 있는 방향으로 1칸 움직였을 때 격자를 벗어난다면
                # 바라보는 방향 반대로 틀기
                # 만약 바라보는 방향으로 움직였을 때 술래가 없다면 1칸 이동

    # 술래가 움직임
        # 이동
            # 처음 위방향으로 시작해 달팽이 모양으로 움직임
            # 끝에 도달하면 다시 거꾸로 중심으로 이동

            # 이동후의 위치가 이동방향이 틀어지는 지점일 경우 방향을 바로 틀어줌
            # 시작점과 끝점에서도 도달하자마자 방향 틀어주기
        # 도망자 잡기
            # 바라보는 방향 기준으로 현재 칸 포함해 3칸을 확인해 도망자 잡기
                # 나무가 놓여져 있는 칸의 도망자는 잡히지 않음
            # 잡힌 도망자는 사라짐
            # 점수 얻기 = 현재 턴 * 현재 턴에서 잡힌 도망자의 수
# n은 반드시 홀수
# answer : k번에 걸쳐 술래잡기 진행하는 동안 술래가 총 얻게된 점수 출력
# ======================================================
# n, m, h, k 입력
n, m, h, k = map(int, input().split())
# m만큼 반복하면서
# 도망자들 저장
runners = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    runners[x - 1][y - 1].append(d)

# 갱신된 도망자들 위치 저장할 변수
next_runners = [[[] for _ in range(n)] for _ in range(n)]

# h만큼 반복하면서
# 나무 위치 x, 나무 위치 y 입력
trees = {}
for _ in range(h):
    tx, ty = tuple(map(int, input().split()))
    trees[(tx - 1, ty - 1)] = True

catcher_x = n // 2
catcher_y = n // 2
catcher_move_direction = [[0] * n for _ in range(n)]
catcher_move_reverse_direction = [[0] * n for _ in range(n)]
catcher_d = 0
# 술래 이동이 정방향인지 역방향인지 여부 변수
isReverse = False

# 방향 리스트(상우하좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 술래 방향 미리 설정 함수
def set_catcher_direction():
    # 방향 리스트(상우하좌)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 현재 위치 = (n // 2, n // 2)
    curr_x = n // 2
    curr_y = n // 2
    # 현재 방향 = 0
    curr_d = 0
    # 이동할 횟수 = 1
    move_num = 1

    while True:
        # 만약 술래가 0,0에 도착했다면
        if curr_x == 0 and curr_y == 0:
            break

        # 이동할 횟수를 반복하면서
        for i in range(move_num):
            # 현재 방향으로 이동
            # 술래 이동 방향 행열에 현재 방향 저장
            catcher_move_direction[curr_x][curr_y] = curr_d

            curr_x += dx[curr_d]
            curr_y += dy[curr_d]

            # 술래 이동 방향 행열에 현재 역방향 저장
            catcher_move_reverse_direction[curr_x][curr_y] = (curr_d + 2) % 4

            if curr_x == 0 and curr_y == 0:
                break

        # 방향 변경(시계방향으로)
        curr_d = (curr_d + 1) % 4

        # 만약 현재 방향이 위또는 아래이면
        if curr_d == 0 or curr_d == 2:
            # 이동할 횟수 증가
            move_num += 1

# 도망자 이동 함수
def runner_move():
    for i in range(n):
        for j in range(n):
            next_runners[i][j] = []

    # 도망자들을 반복하면서
    for i in range(n):
        for j in range(n):
            if abs(i - catcher_x) + abs(j - catcher_y) <= 3:
                for runner_d in runners[i][j]:
                    # 현재 바라보는 방향으로 이동할 위치 계산
                    runner_nx = i + dx[runner_d]
                    runner_ny = j + dy[runner_d]

                    # 만약 격자를 벗어났다면
                    if not in_range(runner_nx, runner_ny):
                        # 바라보는 방향 반대로 틀기
                        runner_d = (runner_d + 2) % 4
                        # 바라보는 방향으로 이동할 위치 계산
                        runner_nx = i + dx[runner_d]
                        runner_ny = j + dy[runner_d]

                    if catcher_x == runner_nx and catcher_y == runner_ny:
                        next_runners[i][j].append(runner_d)
                    else:
                        # 해당 칸으로 이동
                        next_runners[runner_nx][runner_ny].append(runner_d)
            else:
                for runner_d in runners[i][j]:
                    next_runners[i][j].append(runner_d)

    # 도망자 위치 정보 갱신
    for i in range(n):
        for j in range(n):
            runners[i][j] = next_runners[i][j]

# 술래 이동 함수
def catcher_move():
    global isReverse
    global catcher_x
    global catcher_y
    global catcher_d

    # 해당 방향으로 한칸이동
    catcher_x += dx[catcher_d]
    catcher_y += dy[catcher_d]

    # 만약 이동한 위치가 0,0이라면
    if catcher_x == 0 and catcher_y == 0 and not isReverse:
        # 술래 정방향 변수 True로 변경
        isReverse = True
    # elif 정중앙이라면
    elif catcher_x == n // 2 and catcher_y == n // 2 and isReverse:
        # 술래 정방향 변수 False로 변경
        isReverse = False

    # 현재칸 방향에 맞게 현재 술래 방향 변경
    if isReverse:
        catcher_d = catcher_move_reverse_direction[catcher_x][catcher_y]
    else:
        catcher_d = catcher_move_direction[catcher_x][catcher_y]

# 술래 도망자 잡기 함수(현재 턴)
def catcher_score(turn):
    # 잡은 도망자 카운트 변수
    score = 0
    # 바라보는 방향 기준으로 3칸(현재칸포함)을 확인하면서
    for i in range(3):
        nx = catcher_x + dx[catcher_d] * i
        ny = catcher_y + dy[catcher_d] * i

        if in_range(nx, ny) and (nx, ny) not in trees:
            # 도망자 카운트 증가
            score += turn * len(runners[nx][ny])
            # 도망자 리스트에서 해당 도망자 제거
            runners[nx][ny] = []

    return score

# 술래 방향 미리 이동 설정 함수 호출
set_catcher_direction()

# answer 변수
answer = 0
# k번을 반복하면서(1~ k+1)
for i in range(1, k + 1):
    # 도망자 이동 함수
    runner_move()
    # 술래 이동 함수
    catcher_move()
    # answer += 술래 도망자 잡기 함수(현재 턴)
    answer += catcher_score(i)

# answer 출력
print(answer)