# 1:53~
# n : 도시 개수
# m : 버스 개수(간선)
# 모든 도시에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값 구하기

# 플로이드 워셜 알고리즘으로 풀기

n = int(input())
m = int(input())

INF = int(1e9)
# 변수 - 그래프 2차원 리스트
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 그래프 자기자신으로 가는 거는 0으로
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0
# 그래프 비용 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # 문제에서 시작도시와 도착 됫를 연결하는 노선은 하나가 아닐 수도 있다고 했기 때문에 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 버스 개수 만큼 반복하면서
for k in range(1, n + 1):
    # 도시 만큼 반복하면서
    for a in range(1, n + 1):
        # 도시 만큼 반복하면서
        for b in range(1, n + 1):
            # 만약 d(a,b) < d(a,k) + d(k, b)인 경우
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()



