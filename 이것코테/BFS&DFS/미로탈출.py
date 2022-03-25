from collections import deque

#실패
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#상,하,좌,우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        #상,하,좌,우 방문하면서 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx >= n or ny < 0 or ny >= m:
                continue
            #만약 괴물이 있다면
            if graph[nx][ny] == 0:
                continue
            #만약 괴물이 없고 처음 방문한 곳인 경우만 최단 거리 기록
            if graph[nx][ny] == 1:
                #출발지부터 방문한 노드의 거리를 저장(이전노드거리에서 1증가)
                graph[nx][ny] += graph[x][y] + 1
                #방문한 노드 queue에 저장
                queue.append((nx,ny))
    #목적지 노드까지의 최단 거리 리턴
    return graph[n-1][m-1]

print(bfs(0,0))