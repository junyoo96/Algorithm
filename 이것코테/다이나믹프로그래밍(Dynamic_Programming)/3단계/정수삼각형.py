# 답안

answer = 0
n = int(input())
dp = []

# 삼각형 입력받기
for _ in range(n):
    dp.append(list(map(int, input().split())))

# 삼각형 반복하면서
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] += max(up_left, up)

# 삼각형의 마지막에서 선택된 경로의 최대 합 구하기
answer = max(dp[n-1])

print(answer)

# ==============================================================
# 내가푼것
# 9:06~9:19
# 9:19~9:52(46/30)
# 다이나믹 프로그램-bottom up

answer = 0 # answer : 선택된 수의 최대 합
n = int(input()) # n : 삼각형의 크기
dp = [] # dp 테이블 : n*n 리스트 만들고 빈칸은 -1로 채우기

# 삼각형 입력 받기
for i in range(n):
    data = list(map(int, input().split()))
    dp.append(data)
    tmp = n - len(data)
    for j in range(tmp):
        dp[i].append(-1)

# 왼쪽 위, 바로 위에서만 올 수 있음
dx = [-1, -1]
dy = [-1, 0]

# dp테이블 행 반복(1, )
for i in range(1, n):
    # dp 테이블 열 반복
    for j in range(n):
        if dp[i][j] == -1:
            continue
        # 현재 칸으로 올 수 있는 두 방향 반복하면서
        val_max = 0
        for direction in range(2):
            # val_max = 0
            nx = i + dx[direction]
            ny = j + dy[direction]
            # 만약 방향이 dp테이블 범위안에 들어온다면
            if 0 <= nx < n and 0 <= ny < n:
                if dp[nx][ny] != -1:
                    # val_max = max(val_max, 현재 값)
                    val_max = max(val_max, dp[nx][ny])
        # dp테이블 값 += val_max
        dp[i][j] += val_max

# dp테이블의 마지막 행에서 max값 찾기
answer = max(dp[n - 1])  # 주의 - 마지막 행또는 마지막 열에서 최대값 찾을 때 for문 돌리지말고 행또는 열에 대한 리스트 뽑아서 max에 바로 넣기

print(answer)

