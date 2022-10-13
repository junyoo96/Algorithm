# 10:04~ - DP 아이디어 생각못함

# 문자열
    # N개의 a와 M개의 z로 이루어져 있음
    # 알파벳 순서대로 수록되어있음
# 동호가 규완이 사전 몰래 참조
    # 문자열 하나만 볼 수 있음
# answer : 규완이의 사전에서 K번째 문자열이 무엇인지 구하기
    # 규완이의 사전에 수록되어 있는 문자열의 개수가 K보다 작으면 -1 출력

import sys
input = sys.stdin.readline

answer = ""
# n : a 개수
# m : z 개수
n, m, k = map(int, input().split())
# DP 테이블 - 각 자리는 주어진 a와 z 개수 따라 만들 수 있는 문자열의 경우의수를 저장
array = [[1] * (m + 1) for _ in range(n + 1)]
# 각 자리는 주어진 a와 z 개수 따라 만들 수 있는 문자열의 경우의수를 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        array[i][j] = array[i - 1][j] + array[i][j - 1]

# 주어진 a와 z로 만들 수 있는 경우의 수보다 찾고있는 문자열의 인덱스가(K) 더 클경우
if array[n][m] < k:
    print(-1)
else:
    while True:
        # a와 z 둘중에 하나가 모두 사용한 경우에는 나머지는 남아있는 문자로 채우고 종료
        if n == 0 or m == 0:
            answer += "z" * m
            answer += "a" * n
            break

        # 현재 a와 z 개수에서 a의 개수를 하나빼고 만들 수 있는 문자열 경우의 수
        flag = array[n - 1][m]
        # 만약 flag(a의 개수를 하나빼고 만들 수 있는 문자열 경우의 수)가 찾고자하는 문자열의 인덱스보다 크다면
        if k <= flag:
            answer += "a"
            # a사용했으니 n(남아있는 a 개수) 감소
            n -= 1
        # 만약 flag(a의 개수를 하나빼고 만들 수 있는 문자열 경우의 수)가 찾고자하는 문자열의 인덱스보다 작다면
        else:
            answer += "z"
            # z사용했으니 m(남아있는 z 개수) 감소
            m -= 1
            # ?
            k -= flag
    print(answer)