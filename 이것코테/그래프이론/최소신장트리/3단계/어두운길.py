#11:17~11:45
#11:45~12:00
# n: 집 개수
# m : 도로 개수

# 임의의 두 집에 대해 가로등이 켜진 도로만으로 오갈 수 있게 만듬
# 가로등 비활성해 절약할 수 있는 최대 금액 출력
# 도로는 양방향 가능

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
n, m  = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블
# 주의 - 부모 테이블 초기화
for i in range(1, n + 1):
    parent[i] = i
# 도로 입력받기(cost, a, b)
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a + 1, b + 1))
    answer += cost
# 도로 비용기준으로 오름차순 정렬
edges.sort()

# 도로들을 반복하면서
for edge in edges:
    cost, a, b = edge
    # 만약 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        # 두 노드간 union 연산 수행
        union_parent(parent, a, b)
        # 전체 비용에서 사용한 비용 빼기
        answer -= cost

# 답 출력
print(answer)