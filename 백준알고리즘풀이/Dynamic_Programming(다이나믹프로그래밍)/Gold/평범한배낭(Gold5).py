# 11:38~ 12:00 / 12:05~

# n : 물건 개수
    # w : 무게
    # v : 가치
# k : 배낭이 수용가능한 최대 무게
# answer : 배낭에 넣을 수 있는 물건들 가치의 최댓값
# 점화식
    # 현재 최대 가치 = max(현재 가치 + 현재 물건을 넣기 전 수용가능한 최대 가치 값, 이전까지의 최대가치 값)
import sys

# n, k 입력
n, k = map(int, sys.stdin.readline().split())
# 각 물건의 (무게, 가치) 입력
things = [tuple(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
# 2차원 dp 테이블 - 각 수용가능한 무게마다의 최대 가치를 저장
dp = [[0] * (k + 1) for _ in range(n + 1)]

# 물건을 반복하면서
for i in range(1, n + 1):
    # 수용가능한 무게를 1부터 반복하면서
    for j in range(1, k + 1):
        weight, value = things[i - 1]

        # 만약 현재 수용가능한 무게가 현재 물건의 무게보다 작다면
        if j < weight:
            # 이전가지의 최대가치 값 그대로 가져오기
            dp[i][j] = dp[i - 1][j]
        # 만약 현재 수용가능한 무게가 현재 물건의 무게보다 크거나 같다면
        else:
            # (현재 가치 + 현재 물건을 넣기 전 수용가능한 최대 가치 값, 이전까지의 최대가치 값) 중 최대값으로 현재가치의 최대값을 갱신
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

# dp 테이블의 마지막 행, 마지막 열이 있는 값이 가방에 넣을 수 있는 최대 가치
answer = dp[n][k]
print(answer)