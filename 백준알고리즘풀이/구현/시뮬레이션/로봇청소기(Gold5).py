# 12:16~12:50/12:50~1:30

# n, m : 방크기
# 로봇 청소기
    # 만약 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
    # 만약 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    # 만약 바라보는 방향 유지한채로 한칸 후진가능하다면, 1번으로 감
    # 만약 후진한 칸이 벽이라 후진못하면, 작동을 멈춤
    # 만약 주변 4칸 중 청소되지 않은 빈칸이 있다면
    # 반시계 방향으로 90도 회전
    # 바라보는 방향을 기준으로 앞쪽칸이 청소되지 않았다면 한칸 전진
    # 1번으로 돌아감
# 방
    # 빈칸 0, 벽 1
# answer : 로봇 청소기가 작동시작한후 작동 멈출때까지 청소하는 칸의 개수 출력
# =======================================
# n, m 입력
n, m = map(int, input().split())
# 로봇 청소기 좌표 x, y, 방향 d 입력
x, y, d = map(int, input().split())
# 방 상태 입력
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# answer 변수
answer = 0
while True:
    if arr[x][y] == 0:
        # 청소 처리(2)
        arr[x][y] = 2
        # answer 증가
        answer += 1

    is_empty = False
    # 4가지 방향으로 반복하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 이동할 칸이 올바른 범위안에 있고 이동할 칸이 빈칸이라면
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            is_empty = True

    # 만약 청소가 가능한 칸이 있다면
    if is_empty:
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            x = nx
            y = ny
    # else 청소가능하지 않다면
    else:
        # 후진할 칸 계산
        back_d = (d + 2) % 4
        bx = x + dx[back_d]
        by = y + dy[back_d]
        # 만약 후진할 칸이 올바른 범위에 있고 벽이 아니라면
        if 0 <= bx < n and 0 <= by < m and arr[bx][by] != 1:
                x = bx
                y = by
        # 벽이 있다면
        else:
            break

print(answer)