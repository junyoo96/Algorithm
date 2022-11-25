# 11:00~11:08 / 11:08~11:23

from itertools import permutations

# n 입력
n = int(input())
# 배열 입력
data = list(map(int, input().split()))

answer = 0
# permutations을 반복하면서
for p in permutations(data, n):
    s = 0
    # 현재 값 계산
    for i in range(n - 1):
        s += abs(p[i] - p[i + 1])

    # 만약 현재값이 최대값이라면 갱신
    answer = max(answer, s)

print(answer)