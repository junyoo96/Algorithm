#9:27~
#10:16~
# n : 학생 수
# m : 두 학생 성적 비교한 횟수
# 그래프
    # 작은 학생 -> 큰 학생

# answer : 성적 순위를 정확히 알 수 있는 학생 몇명인지

# 어떤 노드가 어떤 노드에 대해서 도달할 수 있다면 성적을 비교할 수 있다는 말이므로,
# 따라서, 한 노드가 이외의 다른 노드들에 도달할 수 있다면 그 노드의 순위를 알 수 있다는 의미
# 이를, 모든 노드에 대해서 확인해야 하기 때문에 모든 노드에 대해 모든 노드까지의 거리를 계산하는 플로이드 워셜 알고리즘 사용

INF = int(1e9)

answer = 0
n, m = map(int, input().split())
# 모든 노드와 모든 노드간의 거리를 나타내는 2차원 그래프 생성(디폴트 INF로)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 그래프에서 자기자신 경로 0으로 변경
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 그래프 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# 노드를 반복하면서
for k in range(1, n + 1):
    # 노드를 반복하면서
    for a in range(1, n + 1):
        # 노드를 반복하면서
        for b in range(1, n + 1):
            # 점화식
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 2차원 그래프 행 반복하면서
for i in range(1, n + 1):
    count = 0 # 한 노드에 대해 몇개의 노드가 연결되는지 확인하는 변수
    # 2차원 그래프 열 반복하면서
    for j in range(1, n + 1):
        # 만약 i에서 j로 가는 노드가 연결되어 있거나 j에서 i로 가는 노드가 연결되어 있는 경우
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    # 만약 현재 노드에 모든 노드가 연결되어 있는 경우
    if count == n:
        # 연결되어 있는 노드 증가(순위 알 수 있는 학생 수 증가)
        answer += 1

print(answer)

