#12:23~12:40
#12:40~

# n : 여행지 수
    # 양방향 이동 가능
# m : 여행 계획 도시 수

# answer : 여행 계획이 가능한지 여부 판별(YES, NO)
# 서로소 집합 알고리즘으로 풀기
    # 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 가능한 여행 경로
    # 두 노드 사이에 도로가 존재하는 경우에는 union 연산을 이용해, 서로 연결된 두 노드를 같은 집합에 속하도록 만듬

# find 함수 - 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 함수 - 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = "YES"
n, m = map(int, input().split())
# 부모 테이블 생성
parent = [0] * (n + 1)
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 각 연결 간선에 대해 union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 연결된 경우 union 연산 수행
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
travel = list(map(int, input().split()))

# 여행 계획을 반복하면서(뒤에서 2번째까지)
for i in range(m - 1):
    a = travel[i]
    b = travel[i + 1]
    # 현재 여행계획에 속하는 모든 노드의 루트노드가 동일한지 확인(동일하지 않다면 서로 연결되어 있지 않다는 의미)
    if find_parent(parent, a) != find_parent(parent, b):
        answer = "NO"
        break

print(answer)