# 1:48~2:09(21분)
# 2:09~2:24(15분)

# 정사각형 모양의 지도가
    # 1 : 집
    # 0 : 집 없는 곳

# 연결된 집의 모임인 단지 정의하고 단지 번호
    # 상하좌우로 다른 집이 있는 경우 연결됐다고 함
# answer
    # 총 단지수
    # 각 단지 내 집의 수 오름차순으로 정렬해 출력

# dfs로 풀기

answer = []
# 크기 입력
n = int(input())
# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# 상우하좌 리스트
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 단지 내 집의 수 카운트할 변수
count = 0

# 함수 dfs(시작좌표) - -1(없는 경우), 1이상(있는 경우)
def dfs(x, y):
    # 만약 현재 좌표가 범위에서 벗어났다면
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 만약 현재 좌표의 값이 1이라면
    if graph[x][y] == 1:
        # 현재 좌표의 값을 0로 바꾸기
        graph[x][y] = 0
        # 단지 내 집의 수 카운트 1 증가
        global count
        count += 1
        # 상우하좌를 반복하면서
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

# 그래프를 반복하면서
for i in range(n):
    for j in range(n):
        # 만약 함수 dfs가 true이면
        if dfs(i, j):
            # answer에 카운트 변수 추가
            answer.append(count)
            # 카운트 변수 0으로 초기화
            count = 0

# 총단지 수 출력
print(len(answer))
# 단지내 집의 수 한줄씩 출력
for i in sorted(answer):
    print(i)