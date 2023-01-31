# 백트래킹 사용해 직접 구현 방식
def dfs(idx):
    if len(s) == m:
        print(*s)

    # 조합은 (1,2)와 (2,1)이 같으므로 현자idx보다 오른쪽에 있는 idx만 처리하도록 start 변수 사용
    for i in range(idx, n):
        s.append(nums[i])
        dfs(i + 1) # 다음숫자가 현재숫자보다 크게 i + 1
        s.pop()

n, m = map(int, input().split())
s = []
nums = [i for i in range(1, n + 1)]
dfs(0)

# #===================================
# combinations 라이브러리 사용 방식
from itertools import combinations

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

for i in combinations(array, m):
    print(*list(i))