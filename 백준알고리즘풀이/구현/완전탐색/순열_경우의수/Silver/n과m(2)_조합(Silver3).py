# 백트래킹 사용해 직접 구현 방식
def dfs(start):
    if len(s) == m:
        print(*s)

    # 조합은 (1,2)와 (2,1)이 같으므로 현재숫자보다 다음숫자가 작거나 같지않게 start 변수 사용
    for i in range(start, n + 1):
        if visited[i]:
            continue

        s.append(i)
        visited[i] = True
        dfs(i + 1)
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs(1)

#===================================
# combinations 라이브러리 사용 방식
from itertools import combinations

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for i in combinations(array, m):
    print(*list(i))