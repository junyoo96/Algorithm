# 10:39~11:28 / 11:28~12:39(일단 다 구현한 시간) /

# n: 격자 크기
# 무기가 있음
# 초기
# 무기들이 없는 빈 격자에 플레이어들이 위치
# 플레이어
# 초기능력치 갖음(모두 다름)
# 위치가 겹쳐져 주어지지 않음
# 플레이어의 초기 위치에는 총이 없음
# 0 빈칸, 0보다 큰값이면 총의 공격력

# 빨간배경 숫자
# 총 : 공격력
# 플레이어 : 초기 능력치
# 노란 배경 숫자 : 플레이어 번호

# 플레이어 수만큼 다음을 반복
# 1. 첫번째 플레이어부터 순차적으로 본인이 향하는 방향대로 한칸씩 이동
# 만약 격자를 벗어나는 경우, 정반대 방향으로 방향으로 바꾸어 1만큼 이동

# 2-1. 만약 이동한 방향에 플레이어가 없다면, 해당 칸에 총이 있는지 확인
# 만약 총이 있는 경우, 해당 플레이어는 총을 획득
# 플레이어가 이미 총을 가지고 있는 경우, 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공력더 쎈 총 획득하고, 나머지 총들은 격자에 둠

# 2-2. 만약 이동한 방향에 플레이어가 있는 경우, 두 플레이어가 싸움
# 플레이어의 초기능력치 + 총의 공격력을 비교해 더 큰 플레이어가 이김
# 만약 해당 수치가 같은 경우, 플레이어 초기능력치가 높은 플레이어가 승리
# 이긴 플레이어는 (각 플레이어 초기 능력치 + 총의 공격력)의 차이 만큼을 포인트로 획득
# 승리한 칸에 떨어져있는 총들과 원래 들고 있던 총 중 가장 공격력 높은 총 획득, 나머지는 총은 해당 격자에 내려놓음

# 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한칸 이동
# 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우, 오른쪽으로 90도 회전하면서 빈칸이 보이는 순간 이동
# 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총 획득하고, 나머지 총은 격자에 내려놓음

# m : 플레이어 수
# k : 라운드 수

# answer : 위의 과정을 라운드 수만큼 반복하면서 각 플레이어들이 획득한 포인트를 출력
# =====================================================
# n,m,k 입력
n, m, k = map(int, input().split())
# answer 변수 - 리스트
answer = [0] * m

# n * n 이중 리스트 생성
# 주의 - 빈칸 있는 이중 리스트 생성 방법
gun = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# n만큼 반복하면서
for i in range(n):
    # 각 칸을 반복하면서
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0: # 주의 - 0인 경우는 총이 없음으로 제외해야함
            # 해당 칸마다 리스트 생성하고 총 숫자 추가해서 넣기
            gun[i][j].append(tmp[j])

# 플레이어 리스트 생성
players = []
# m만큼 반복하면서
for i in range(m):
    x, y, d, s = map(int, input().split())
    # 입력받은거 마지막에 0(총의 능력치)까지 해서 리스트에 추가
    players.append((i, x - 1, y - 1, d, s, 0))

# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

EMPTY = (-1, -1, -1, -1, -1, -1)

# 좌표 범위 올바른지 여부 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동할 좌표와 방향 계산 함수
def get_next(x, y, d):
    # 향한 방향으로 이동할 좌표 계산
    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    return nx, ny, d

# 플레이어 이동 함수
def move(player, nx, ny):

    num, x, y, d, s, g = player

    # 가장 좋은 총으로 갱신
    # 중요 - 총 갱신 방법
    gun[nx][ny].append(g)
    gun[nx][ny].sort(reverse=True)
    best = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    player = (num, nx, ny, d, s, best)
    # 플레이어 정보 갱신
    update(player)

# 플레이어 존재 여부 함수(이동한 좌표)
def player_check(nx, ny):
    # 플레이어 리스트를 반복하면서
    for idx, player in enumerate(players):
        _, x, y, _, _, _ = player
        # 만약 이동한 좌표에 플레이어가 있다면
        if nx == x and ny == y:
            return players[idx]

    return EMPTY

# 플레이어 정보 갱신 함수
def update(player):
    num = player[0]

    for i in range(m):
        num_i = players[i][0]

        if num_i == num:
            players[i] = player
            break

# 싸움에서 진 플레이어 이동함수
def lose_player_move(lose_player):
    num, x, y, d, s, g = lose_player

    # 먼저 해당 칸에 총 내려놓기
    gun[x][y].append(g)

    # 오른쪽으로 90도 회전하면서 만약 이동하려는 칸에 다른 플레이어가 없고 올바른 범위인 경우 이동
    for i in range(4):
        nd = (d + i) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if in_range(nx, ny) and player_check(nx, ny) == EMPTY:
            player = (num, x, y, nd, s, 0)
            move(player, nx, ny)
            break

# 싸움 함수
def fight(x, y, player, encounter_player):
    # 현재 플레이어의 초기능력치, 총 능력치
    num, _, _, _, s, g = player
    # 해당 칸 플레이어의 초기능력치, 총 능력치
    encounter_num, _, _, _, encounter_s, encounter_g = encounter_player

    if (s + g, s) > (encounter_s + encounter_g, encounter_s):
        answer[num] += (s + g) - (encounter_s + encounter_g)
        lose_player_move(encounter_player)
        move(player, x, y)
    else:
        answer[encounter_num] += (encounter_s + encounter_g) - (s + g)
        lose_player_move(player)
        move(encounter_player, x, y)

# k만큼 라운드를 반복하면서
for _ in range(k):
    # 플레이어 수 만큼 반복하면서
    for player_idx in range(m):
        num, x, y, d, s, g = players[player_idx]

        # 1. 이동할 좌표와 방향 계산
        nx, ny, nd = get_next(x, y, d)

        # 2. 플레이어 존재 확인
        next_player = player_check(nx, ny)

        # 3. 현재 플레이어 정보 갱신
        curr_player = (num, nx, ny, nd, s, g)
        update(curr_player)

        # 4. 플레이어 존재 여부에 따라 처리
        # 만약 플레이어가 없다면
        if next_player == EMPTY:
            # 이동 함수 호출
            move(curr_player, nx, ny)
        else:
            # 싸움 함수 호출
            fight(nx, ny, curr_player, next_player)

# answer 출력(리스트 요소를 공백으로 구분해서 호출)
print(*answer)

