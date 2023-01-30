# 백트래킹 사용해 직접 구현 방식
def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
s = []

dfs()

#====================================
# product 라이브러리 사용 방식
from itertools import product

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for i in product(array, repeat=m):
    print(*list(i))