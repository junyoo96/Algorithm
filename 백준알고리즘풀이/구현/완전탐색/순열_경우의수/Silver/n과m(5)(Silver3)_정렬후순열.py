# 백트래킹 사용해 직접 구현 방식
def dfs():
    if len(s) == m:
        print(*s)

    for i in nums:
        if visited[i]:
            continue

        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
visited = [False] * 10001

dfs()

#===================================
# permutations 라이브러리 사용 방식
from itertools import permutations

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

for i in permutations(array, m):
    print(*list(i))