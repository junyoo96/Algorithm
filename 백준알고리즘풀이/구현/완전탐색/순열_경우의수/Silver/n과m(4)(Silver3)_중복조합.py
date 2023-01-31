# 백트래킹 사용해 직접 구현 방식
def dfs(idx):
    if len(s) == m:
        print(*s)
        return

    for i in range(idx, n):
        if i >= idx:
            s.append(nums[i])
            dfs(i)
            s.pop()


n, m = map(int, input().split())
s = []
nums = [i for i in range(1, n + 1)]
dfs(0)

#====================================
# combinations_with_replacement 라이브러리 사용 방식
from itertools import combinations_with_replacement

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for i in combinations_with_replacement(array, m):
    print(*list(i))