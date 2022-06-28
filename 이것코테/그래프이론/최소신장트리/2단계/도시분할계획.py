# find 연산(특정 원소가 속한 집합 찾기)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산(두 원소가 속한 집합 합치기)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기

v, e = map(int, input().split())
parent = [0] * (v + 1)

#모든 간선을 담을 리스트
edges = []
#최종 비용을 담을 변수
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
    # a : 특정 노드 A 번호
    # b : 특정 노드 B 번호
    # cost : 노드 A와 B간의 거리(비용)
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

#최소 신장 트리 알고리즘을 위해 비용 기준으로 간선을 오름차순 정렬
edges.sort()

# 최종 신장 트리가 완성되었을 때 가장 큰 비용을 저장
max_cost = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(루트노드가 다르다는 것은 포함된 집합이 다르다는 것을 의미)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # 어차피 비용순으로 정렬되어 있기 때문에 마지막 비용이 가장 큰 비용
        max_cost = cost

# 문제에서 2개의 최소 신장 트리를 만드는 것이기 때문에 가장 큰 비용을 가진 간선을 빼서 분리하기
result -= max_cost

print(result)



