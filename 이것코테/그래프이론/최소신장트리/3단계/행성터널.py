# 10:35~10:53
# 10:53~

# n : 행성 개수
# answer : 모든 행성을 터널로 연결하는데 필요한 최소 비용

# 최소 신장 트리 알고리즘으로 풀기

# find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
# 입력
n = int(input())
edges = [] # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
parent = [0] * (n + 1) # 부모 테이블
# 부모 테이블을 자기자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

x = [] # 각 노드의 x좌표 저장
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

# 고려할 간선의 개수를 줄이기 위해
    # 각 축에 대해 따로 간선을 고려하기 위해 각 축에 대해 따로 오름차순 정렬
x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정 
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 반복하면서
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        # union 연산 실행
        union_parent(parent, a, b)
        # answer 증가
        answer += cost

# 답 출력
print(answer)