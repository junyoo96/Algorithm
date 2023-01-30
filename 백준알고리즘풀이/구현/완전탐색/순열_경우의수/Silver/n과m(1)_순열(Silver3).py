# 백트래킹 사용해 직접 구현 방식
def dfs():
    if len(s) == m:
        print(*s)

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()

#===================================
# permutations 라이브러리 사용 방식
from itertools import permutations

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for i in permutations(array, m):
    print(*list(i))