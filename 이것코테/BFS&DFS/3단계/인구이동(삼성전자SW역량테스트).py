# 9:08~ 9: 57
# 9:57~
from collections import deque

# n : 땅 크기
# L, R : 인구차이 조건
n, l, r = map(int, input().split())

# 변수 - 나라 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신하는 함수
def process(x, y, index):
    # 연합에 속하는 나라의 위치(x, y)를 저장하는 리스트
    united = []
    united.append((x,y))
    # 너비 우선 탐색(BFS)를 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))

    # 현재 나라에 연합의 번호 할당
    union[x][y] = index
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 나라 수

    # 큐가 빌때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여, 나라 칸에서 벗어나지 않고, 아직 해당 나라에 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny)) # 큐에 해당 좌표 추가
                    # 연합에 추가
                    union[nx][ny] = index
                    # 연합의 인구수 더하기
                    summary += graph[nx][ny]
                    # 연합의 나라 수 더하기
                    count += 1
                    # 연합에 속한 나라들의 위치 저장하는 리스트에 추가
                    united.append((nx,ny))

    # 연합 국가 끼리 인구수 분배
    for i, j in united:
        graph[i][j] = summary // count

    return count

total_count = 0 # 총 인구 이동 수

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)] # 각 나라의 연합 번호 저장할 2차원 리스트(-1은 방문 안한 나라)
    index = 0 # 연합 번호 카운트
    for i in range(n):
        for j in range(n):
            # 해당 나라가 아직 처리되지 않았다면
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
