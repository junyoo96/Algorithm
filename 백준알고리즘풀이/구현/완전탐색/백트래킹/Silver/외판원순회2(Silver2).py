# 11:36~12:05 / 12:05~ - 아이디어는 맞았고 구현은 거의 맞았는데 주의 코드 로직을 놓쳐서 못했음
# 11:35~11:58 / 11:58~
#============================================================================
# 최적화 코드 - 백트래킹(이걸로 풀기)
import sys

# 도시의 개수 입력
N = int(input())
# 경로 비용 입력
travel_cost = [list(map(int, input().split())) for _ in range(N)]
#출력할 최소값 정의
min_value = sys.maxsize

# 시작도시번호,다음도시번호,비용,방문 도시
def dfs_backtracking(start, next, value, visited):
    global min_value

    # 만약 방문한 도시가 전체 도시의 개수와 같다면 순회 완료했다는 의미이므로
    if len(visited) == N:
        # 주의 - 마지막 도시에서 출발 도시로 가는 길이 있다면
        if travel_cost[next][start] != 0:
            # 현재까지의 비용에 출발도시로 가는 비용을 더해서 최소값과 비교해 갱신
            min_value = min(min_value, value + travel_cost[next][start])
        return

    # 도시의 개수만큼 반복하면서
    for i in range(N):
        # 만약 현재 도시에서 가는 다음도시로 가는 길이 있고, 이미 방문한 도시가 아니며 , 그 비용값이 저장되어있는 최소값보다 작다면(제일 중요!!!, 이거 때문에 backtracking이 제대로 되어서 시간이 단축되는 거임)
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            # 다음 도시를 방문목록에 추가
            visited.append(i)
            # 다음 도시 방문
            dfs_backtracking(start, i, value + travel_cost[next][i], visited)
            # 방문을 완료했다면 방문목록 해제
            visited.pop()

# 도시마다 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)

#===================================================================
# 내 코드 - 순열
# 11:35~11:58 / 11:58~12:21

# n : 도시 개수(2~10)
# 도시들 사이에 길(없을 수 있음 0)
# 어느 한도시에서 출발해 N개 도시거쳐 다시 원래도시로 돌아오기
# 한번 갔던 도시로는 다시 갈 수 없음
# 비용
# 도시간 비용은 양의 정수
# answer : 가장 적은 비용을 들이는 여행 계획
# ===================================
from itertools import permutations

# answer
answer = 1e9
# n 입력
n = int(input())
# 도시 비용 입력
arr = [list(map(int, input().split())) for _ in range(n)]

# 경로 permutations 반복하면서
# 중요 - 그냥 permutations로 풀면 시간초과 나지만 어느도시에서 시작하든 순회가능이 보장되어있기 때문에 어느 도시에서 순회를 시작하든 같은 경로이므로 , 하나의 시작도시에 대해서만 체크해 시간초과 해결
# 시작도시 1을 제외한 나머지 경로 순열 만들기
cities = [i for i in range(2, n + 1)]
roads = []
for p in permutations(cities, len(cities)):
    # 시작도시 1에 대해서만 체크
    roads.append([1] + list(p) + [1])

for road in roads:
    # 현재 경로의 합 변수
    s = 0
    isTraverse = True
    # combination의 도시를 순회하면서
    for i in range(len(road) - 1):
        start = road[i]
        end = road[i + 1]
        # 만약 도시간의 길이 없다면
        if arr[start - 1][end - 1] == 0:
            # break
            isTraverse = False
            break

        s += arr[start - 1][end - 1]
    # 만약 현재 경로 비용의 합이 최소값이라면 갱신
    if isTraverse:
        answer = min(answer, s)

# answer 출력
print(answer)