# 문제이해 / 아이디어 / 구현 / 디버깅
# 9:58~10:21 / 11:05~12:04/ 12:04~1:24/ 1:24~

# n : 격자 크기
    # 빈칸 0, 벽 -1
# 제초
    # k : 제초제 확산 범위
    # 벽이 있으면 가로막혀서 전파되지 않음

# 1년 과정
    # 성장
    # 1. 인접한 4개의 칸 중 나무가 있는 칸 수만큼 나무 성장 (동시에 일어남)
    # 2. 기존 나무들은 인접한 4개 칸 중 벽, 다른나무, 제초제 모두 없는 칸에 번식 진행
        # 인접한 각 칸에 번식할 나무 수 = 현재 칸의 나무 그루 수 // 총 번식이 가능한 칸의 개수 (동시에 일어남)
    # 제초
    # 3. 나무가 가장 많이 박멸되는 칸에 제초제 뿌림
        # 제초제를 뿌릴 때 4개의 대각선 방향으로 k칸만큼 전파되게 됨
        # 가장 많은 나무를 박멸시키는 칸을 계산해서 제초를 뿌림
        # 박멸시키는 나무수가 동일한 칸이있으면, 행이 작은 순, 열이 작은 순대로 선택
        # 전파도중 벽이나 나무가 아예없는 칸이 있는 경우, 그 칸까지는 제초지 뿌림
        # 제초지가 뿌려진 칸에는 c년만큼 제초제가 남아있다 c+1년 째가 될 때 사라짐
        # 원래 제초제 뿌려진 곳에 다시 뿌릴 경우 새로 뿌려진 해부터 다시 c년동안 제초제 유지
# answer : m년 동안 총 박멸한 나무 그루 수
# ================================================

from copy import deepcopy

n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
remover_arr = [[0] * n for _ in range(n)]
# 상우하좌 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 대각선 좌표(북서, 복동, 남동, 남서)
d_dx = [-1, -1, 1, 1]
d_dy = [-1, 1, 1, -1]
# 총 박멸한 나무의 그루 수
answer = 0

# 나무 성장
def grow():
    # 격자 행열을 반복하면서
    for i in range(n):
        for j in range(n):
            # 만약 나무라면
            if arr[i][j] > 0:
                # 인접한 칸을 반복하면서
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if (0 <= nx < n and 0 <= ny < n) and arr[nx][ny] > 0:
                        arr[i][j] += 1

# 주변 나무 번식
def reproduce():
    # 번식할 나무 수를 저장할 변수
    tmp = deepcopy(arr)

    # 격자 행열을 반복하면서
    for i in range(n):
        for j in range(n):
            # 만약 나무라면
            if arr[i][j] > 0:
                # 번식할 숙주 나무의 양
                tree_amount = arr[i][j]
                # 번식이 가능한(벽, 다른 나무, 제초제 모두 없는 칸)의 개수
                cnt = 0

                # 인접한 칸을 반복하면서
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    # 만약 올바른 범위 내에 있다면
                    if 0 <= nx < n and 0 <= ny < n:
                        # 만약 인접한 칸이 빈칸이고 제초제가 없다면
                        if arr[nx][ny] == 0 and remover_arr[nx][ny] == 0:
                            # 번식 가능한 개수 증가
                            cnt += 1

                # 주의 - 번식 가능한 칸에 대해 번식물 수를 갱신하는 과정
                # 만약 번식 가능한 칸이 한칸이라도 있다면
                if cnt != 0:
                    # 번식할 나무 수 계산
                    tree_spread_amount = tree_amount // cnt

                    # 인접한 칸에 나무 번식
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]

                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 0 and remover_arr[nx][ny] == 0:
                                tmp[nx][ny] += tree_spread_amount

    return tmp

# 가장 많은 나무를 죽일 수 있는 위치를 찾는 함수
# 중요 - 대각선 이동 어떻게 처리 하는지 잘보기
def get_remove_position(x, y):
    global k_x, k_y, kill_amount

    # 제초제로 죽일 수 있는 나무의 양
    value = arr[x][y]

    # 대각선을 반복하면서
    for d in range(4):
        # 중요 - 대각선 이동 처리
        cur_x, cur_y = x, y
        # 대각선 범위 만큼 반복하면서
        for _ in range(k):
            # 인접 칸 좌표 계산
            nx = cur_x + d_dx[d]
            ny = cur_y + d_dy[d]

            # 만약 올바른 범위 내에 있지 않다면 break
            if not (0 <= nx < n and 0 <= ny < n):
                break

            # 만약 나무가 아니라면 break
            if arr[nx][ny] <= 0:
                break

            # 만약 나무라면
            if arr[nx][ny] > 0:
                # 제초제로 죽일 수 있는 나무의 양에 더하기
                value += arr[nx][ny]
                # 중요 - 현재 좌표 갱신
                cur_x, cur_y = nx, ny

    # 만약 현재 박멸 수가 기존 최대 박멸수보다 크다면
    if value > kill_amount:
        # 최대 박멸 좌표 갱신
        k_x, k_y = x, y
        # 최대 박멸 수 갱신
        kill_amount = value

# 최대 박멸 칸을 기준으로 제초제를 뿌려 나무를 제거하는 함수
def remove_tree(x, y):

    # 제초제 행열의 최대 박멸 칸을 새로운 제초제 기간으로 갱신
    remover_arr[x][y] = c
    # 제초제 뿌렸으니 해당 칸 나무 제거
    arr[x][y] = 0

    # 대각선 방향으로 나무 제거
    for d in range(4):
        # 현재 위치 갱신
        cur_x, cur_y = x, y
        # 제초제 확산 범위 만큼 반복하면서
        # 중요 - 대각선 방향을 먼저 반복하고 그안에서 제초제 확산 범위를 반복하면서, 빈칸이나 벽일 경우 그 방향으로 더이상 처리가 진행되지 않는 것을 구현
        for _ in range(k):
            # 대각선 인접 칸 좌표 계산
            nx = cur_x + d_dx[d]
            ny = cur_y + d_dy[d]

            # 만약 올바른 범위 내에 있지 않다면
            if not (0 <= nx < n and 0 <= ny < n):
                break

            # 만약 인접 칸이 벽이라면 제초제 안뿌려도 됨
            if arr[nx][ny] == -1:
                break

            # 만약 인접 칸이 빈칸이라면 제초제는 뿌리고 더이상 진행안됨
            if arr[nx][ny] == 0:
                # 제초제 뿌리긴 했으니 해당 칸을 제초제 유효기간으로 갱신
                remover_arr[nx][ny] = c
                break

            # 만약 인접 칸이 나무라면
            if arr[nx][ny] > 0:
                # 해당 칸에 제초제 표시
                remover_arr[nx][ny] = c
                # 격자 행열의 해당 칸에 나무 제거
                arr[nx][ny] = 0
                # 현재 좌표 갱신
                cur_x, cur_y = nx, ny

# 제초제 시간 줄이는 함수
def reduce_remover_time():
    # 격자 행열을 반복하면서
    for i in range(n):
        for j in range(n):
            # 만약 제초제가 있는 칸이라면
            if remover_arr[i][j] > 0:
                # 주의 - 제초제 남은년수 감소
                remover_arr[i][j] -= 1

# m년 동안 총 박멸한 나무의 그루 수 구하기
for _ in range(m):

    # 나무 성장
    grow()

    # 나무 주변 번식
    arr = reproduce()

    # 가장 많이 박멸되는 칸 찾기
    k_x, k_y = 0, 0 # 가장 많이 박멸되는 칸 좌표
    kill_amount = 0 # 최대 박멸 수
    # 격자 행열을 반복하면서
    for i in range(n):
        for j in range(n):
            # 주의 - 만약 빈칸이라면
            if arr[i][j] > 0:
                get_remove_position(i, j)

    # 제초제 시간 줄이기
    reduce_remover_time()

    # 제초제 살포
    remove_tree(k_x, k_y)

    # 박멸한 나무 그루수에 더하기
    answer += kill_amount

print(answer)

