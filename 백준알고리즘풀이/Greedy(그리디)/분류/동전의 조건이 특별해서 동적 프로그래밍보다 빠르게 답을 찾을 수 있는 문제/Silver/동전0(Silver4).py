# 10:14~10:18 / 10:18~10:23

# n : 동전 종류
# K : 가치의 합
# answer : K를 만들기 위한 동전 개수의 최솟값
#==============================
import sys
input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())
# n만큼 동전 가치 입력
coins = [int(input()) for _ in range(n)]

# answer 변수
answer = 0
# 동전종류를 거꾸로 반복하면서
for i in range(len(coins) - 1 , -1, -1):
    # 만약 k가 0이라면
    if k == 0:
        # break
        break

    # k를 현재 동전종류를 나눈 몫을 answer에 더하기
    answer += k // coins[i]
    # k를 현재 동전종류를 나눈 나머지로 갱신
    k %= coins[i]

# answer 출력
print(answer)