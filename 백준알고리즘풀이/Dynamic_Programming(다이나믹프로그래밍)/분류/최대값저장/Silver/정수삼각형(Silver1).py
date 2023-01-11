# n : 삼각형 크기
# 아래층으로 내려오면서 합 더하기
# answer : 선택된 수의 합의 최대 합

#================================================================
# 답안코드
#================================================================
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
# 내 코드
# ==============================================================
# 9:06~9:19 / 9:19~9:52(46/30)
# 10:17~10:33 / 10:33~10:51(34/30)

# 다이나믹 프로그램-bottom up
import sys

answer = 0 # answer : 선택된 수의 최대 합
n = int(sys.stdin.readline()) # n : 삼각형의 크기
# n 크기의 dp 테이블 생성하면서 모두 -1로 채우기
dp = [[-1] * n for _ in range(n)]
# n만큼 반복하면서
for i in range(n):
    # 삼각형 입력 받기
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(tmp)):
        dp[i][j] = tmp[j]

# 왼쪽 위, 바로 위에서만 올 수 있음
dx = [-1, -1]
dy = [-1, 0]

# dp테이블 행 1부터 반복하면서
for i in range(1, n):
    # dp 테이블 열 반복하면서
    for j in range(n):
        if dp[i][j] != -1:
            # 현재 위치 수 저장
            value = dp[i][j]
            # 2방향을 반복하면서
            for d in range(2):
                nx = i + dx[d]
                ny = j + dy[d]
                # 만약 현재 위치가 올바른 범위라면(범위안에 있고 -1이 아니라면)
                if (0 <= nx < n and 0 <= ny < n) and dp[nx][ny] != -1:
                    # 현재 위치수까지의 합 계산해서 최댓값 갱신
                    dp[i][j] = max(dp[i][j], dp[nx][ny] + value)

# dp테이블의 마지막 행에서 max값 찾기
answer = max(dp[n - 1])  # 주의 - 마지막 행또는 마지막 열에서 최대값 찾을 때 for문 돌리지말고 행 또는 열에 대한 리스트 뽑아서 max에 바로 넣기
print(answer)