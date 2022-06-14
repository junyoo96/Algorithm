#11:30~

# n : 2차원 공간 크기
    # 각각의 칸 지나기 위한 비용
# answer : 0,0에서 n-1,n-1까지 이동하는 최소 비용
    # 상하좌우로 1칸씩 이동 가능

# 다익스트라 알고리즘 사용
    # 한 지점에서 한 지점으로 가는 최단 거리 구하는 문제이기 때문

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 테스트 케이스 수 입력
tc = int(input())

# 테스트 케이스 반복하면서
for _ in range(tc):

    n = int(input())
    # 2차원 그래프 생성
    graph = []
    # 그래프 입력받기
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 2차원 distance 테이블
    distance = [[INF] * n for i in range(n)]

    # 다익스트라 알고리즘 수행
    # heapq에 (출발지점 비용하고, 출발좌표) 넣기
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    # 출발지점에서 사용되는 비용
    distance[x][y] = graph[x][y]

    # 큐가 차있을 때까지 반복하면서
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        # 만약 현재 노드가 이미 방문된 경우 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 반복하면서(상우하좌)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 움직인 좌표가 맵의 범위를 벗어나는 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 움직인 좌표 까지의 비용을 계산
                cost = dist + graph[nx][ny]
                # 만약 움직인 좌표까지의 비용이 기존 distance에서 움직인 좌표까지의 비용보다 작을 경우
                if cost < distance[nx][ny]:
                    # distance 테이블의 현재 좌표까지의 비용을 갱신
                    distance[nx][ny] = cost
                    # 방문한 좌표들 heapq에 넣기
                    heapq.heappush(q, (cost, nx, ny))

    # 목적지 값을 출력
    print(distance[n-1][n-1])




