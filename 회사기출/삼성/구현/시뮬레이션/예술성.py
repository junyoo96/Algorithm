# 9:35~10:50(회전부분빼고) / 10:50~11:15(회전부분 빼고) 실패

# n : 그림 크기
# 각 칸 색깔 1~10
# 상하좌우로 인접해있는 경우 동일한 그룹으로 처리
# 예술점수
# 초기 예술 점수 : 각 그룹간의 조화로움의 합을 의미
# 조화로움 : (그룹 a에 속한 칸 수 + 그룹 b에 속한 칸수) * 그룹 a를 이루고 있는 숫자값 *  그룹 b를 이루는 숫자값 * 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
# 그림에 대한 회전 진행
# 십자모양부분은 반시계 방향으로 90도 회전
# 나머지 4개 정사각형은 각각 개별적으로 시계방향으로 90도 회전
# 예술 점수 구하기

# answer : 초기 + 1회전 + 2회전 + 3회전 예술 점수의 합
# ===================================================================
# n 입력
n = int(input())
# 그림 저장
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 회전한 그림 저장
next_arr = [
    [0] * n
    for _ in range(n)
]

# 그룹의 개수를 저장
group_n = 0

# 각 칸에 그룹 번호 표시
group = [
    [0] * n
    for _ in range(n)
]
# 각 그룹마다 칸의 개수 세기
group_cnt = [0] * (n * n + 1)
# 방문 여부 확인
visited = [
    [False] * n
    for _ in range(n)
]
# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 올바른 범위인지 확인 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# dfs 함수
def dfs(x, y):
    # 4가지 방향을 반복하면서
    for i in range(4):
        # 이동할 좌표 계산
        nx, ny = x + dx[i], y + dy[i]
        # 만약 이동할 좌표가 올바른 범위 내에 있고 숫자가 동일하고 방문한 적이 없는 칸이라면
        if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            # 방문 처리
            visited[nx][ny] = True
            # 해당 좌표는 그룹 표시
            group[nx][ny] = group_n
            # 해당 그룹의 칸 수 저장
            group_cnt[group_n] += 1
            # dfs 호출
            dfs(nx, ny)

# 그룹을 형성하기
def make_group():
    global group_n

    group_n = 0

    # 방문 여부 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 그룹 묶는 작업 진행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                # 그룹 표시
                group[i][j] = group_n
                # 해당 그룹의 칸 수 저장
                group_cnt[group_n] = 1
                # dfs 호출
                dfs(i, j)

# 예술 점수 계산 함수
def get_art_score():
    art_score = 0

    # 특정 변을 사이에 두고 두 칸의 그룹이 다른 경우라면,
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    # 만큼 예술 점수가 더해짐
    # 즉, 예술점수 구하는 방식을 변의 개수를 for문으로 풀어서 처리했음
        # 원래공식 : 예술점수 = (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 * 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
        # 코드에서의 처리
            # 그룹끼리 맞닿아 있는 횟수 만큼 반복하면서
                # 예술점수 += (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                # 만약 인접한 좌표가 올바른 범위 내에 있고 현재좌표와 인접한 좌표가 다르다면(특정 변을 사이에 두고 있다면)
                if in_range(nx, ny) and arr[i][j] != arr[nx][ny]:
                    # 각 칸의 그룹을 확인
                    g1, g2 = group[i][j], group[nx][ny]
                    # 각 칸의 숫자값을 확인
                    num1, num2 = arr[i][j], arr[nx][ny]
                    # 각 그룹을 이루고 있는 칸의 개수 확인
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]
                    # 예술점수 계산
                    art_score += (cnt1 + cnt2) * num1 * num2

    # 중복 계산을 제외해줌
        # 예를 들어 (0,0), (0,1)이 특정 변을 사이에 두고 있다면,
        # (0,0) 차례 때 변 개수를 증가하고, 또 (1,1) 차례 때 변 개수를 증가시켜 2번 중복해 증가시키기 때문
    return art_score // 2

# 예술 점수 계산 함수
def get_score():
    # 그룹 형성
    make_group()

    # 예술 점수 계산
    return get_art_score()

# 정사각형 회전
# sx, sy : 회전하려는 영역의 맨 왼쪽위 좌표
# square_n : 회전하려는 영역의 길이
def rotate_square(sx, sy, square_n):
    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_n):
        for y in range(sy, sy + square_n):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) -> (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_n - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            next_arr[rx + sx][ry + sy] = arr[x][y]

# 중요
def rotate():
    # Step 1. next arr값을 초기화
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    # Step 2. 회전을 진행

    # Step 2 - 1. 십자 모양에 대한 반시계 회전을 진행
    for i in range(n):
        for j in range(n):
            # Case 2 - 1. 세로줄 처리
            # 세로줄에 대해서는 (i, j) -> (j, i)가 됩니다.
            if j == n // 2:
                next_arr[j][i] = arr[i][j]
            # Case 2 - 2. 가로줄 처리
            # 가로줄에 대해서는 (i, j) -> (n - j - 1, i)가 됩니다.
            elif i == n // 2:
                next_arr[n - j - 1][i] = arr[i][j]

    # Step 2 - 2. 4개의 정사각형에 대해 시계 방향 회전을 진행
    square_n = n // 2
    # 왼쪽위 정사각형 회전
    rotate_square(0, 0, square_n)
    # 오른쪽위 정사각형 회전
    rotate_square(0, square_n + 1, square_n)
    # 왼쪽밑 정사각형 회전
    rotate_square(square_n + 1, 0, square_n)
    # 오른쪽밑 정사각형 회전
    rotate_square(square_n + 1, square_n + 1, square_n)

    # Step 3. next arr값을 다시 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

# 3회전까지의 예술 점수를 더하기
answer = 0
for _ in range(4):
    # 현재 예술 점수를 더하기
    answer += get_score()

    # 그림 회전을 진행
    rotate()

print(answer)