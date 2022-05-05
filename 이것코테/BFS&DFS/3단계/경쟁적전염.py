#12:13~ 12:45
#12:46~
#조건
    # 초마다 상,하,좌,우 방향으로 증식
    # 번호가 낮은 종류의 바이러스부터 먼저 증식
    # 이미 바이러스가 있다면 다른 바이러스가 들어갈 수 없음
    # S초가 지난후에 (x-행,y-열)에 존재하는 바이러스 종류 출력
        # 1,1이 가장 왼쪽 위
    # 바이러스가 존재하지 않는다면 0 출력

from collections import deque

# n: 시험관 크기
# k: 바이러스 종류 수
n, k = map(int, input().split())
# 시험관
graph = []
# 바이러스 정보
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스 정보 넣기(바이러스 종류, 해당 바이러스가 몇초 지난 후 갱신됐는지, 바이러스위치 x, y)
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 바이러스 종류 번호가 낮은 순대로 정렬
data.sort()
# BFS를 구현하기 위한 queue
virus_q = deque(data)

# target_s: 출력할 시간
# target_x, taget_y: 바이러스 종류 출력할 위치
target_s, target_x, target_y = map(int, input().split())
# 문제에서 맨왼쪽위가 1,1이라고 했기 때문에 0,0으로 맞추기 위해 -1 해줌 - 주의
target_x = target_x - 1
target_y = target_y - 1

# 바이러스 방향(상,우,하,좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
# queue가 빌 때까지 반복
while virus_q:
    # 바이러스 정보 넣기(바이러스 종류, 해당 바이러스가 몇초 지난 후 갱신됐는지, 바이러스위치 x, y)
    virus, s, x, y = virus_q.popleft()
    # 만약 현재 지나간 시간이 target_s초 이라면 종료
    if s == target_s:
        break

    # 현재 위치에서 4방향 반복하면서 증식 - for
    for i in range(4):
        # nx, ny : 방향대로 이동한 위치
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 이동한 위치가 시험관에서 벗어나지 않는다면
        if 0 <= nx and nx < n and 0 <= ny and ny < n: # 주의 - 괄호
            # 위치가 비어있다면(0)
            if graph[nx][ny] == 0:
                # 현재 바이러스 종류로 갱신
                graph[nx][ny] = virus
                # 갱신한 바이러스 위치 리스트에 집어넣기
                    # 집어넣고 난 다음 바이러스 번호가 낮은순대로 sort해줄 필요가 없는 이유는,
                    # 처음에 위에서 virus_q에 들어갈때 virus 번호가 낮은 순대로 들어가기 때문에
                    # 그 이후 부터는 처리될 때 virus 번호가 낮은 순대로 queue에 들어가기 때문
                virus_q.append((virus, s + 1, nx, ny))

# 주어진 좌표에 해당하는 바이러스 종류 출력
print(graph[target_x][target_y])