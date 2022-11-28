# DP 적용 코드(이걸로 풀기)
    # 점화식
        # P(n) = P(n - 1) + P(n - 2) + P(n - 3) (n >= 4)
        # 초기값
            # P(1) = 1, P(2) = 2, P(3) = 4

t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 점화식 초기값
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            # 점화식
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    answer = dp[n]
    print(answer)
#================================================
# 내 코드 - 중복순열 사용
# 9:05~ 10:00 / 10:00~ - 중복순열 개념 몰라서 라이브러리 확인하고 풀음
from itertools import product

# t 입력
t = int(input())

# t만큼 반복하면서
for _ in range(t):
    answer = 0
    # n 입력
    n = int(input())
    # n에서 1까지 반복하면서
    for i in range(n, 0, -1):
        # 중복순열 반복하면서
        for c in product([1, 2, 3], repeat = i):
            # 만약 합이 n이라면
            if sum(list(c)) == n:
                # answer += 1
                answer += 1

    print(answer)