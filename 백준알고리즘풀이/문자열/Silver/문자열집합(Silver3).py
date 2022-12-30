# 최적화 코드
# 시간 : 128ms
import sys
input = sys.stdin.readline

# n(1~10000)
# m(1~10000)
n, m = map(int, input().split())

# 중요 - set 사용
words = set([input() for _ in range(n)])

answer = 0
for _ in range(m):
    word = input()
    if word in words:
        answer += 1

print(answer)

#=============================================
# 내 코드
# 10:34~10:40 / 10:40~10:44
# 시간 : 3700ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# list 사용
words = set([input() for _ in range(n)])

answer = 0
for _ in range(m):
    word = input()
    if word in words:
        answer += 1

print(answer)
