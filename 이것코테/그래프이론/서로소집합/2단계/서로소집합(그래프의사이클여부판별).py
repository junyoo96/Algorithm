# find 연산 : 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 : 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

#사이클 발생 여부
cycle = False

#주어진 union 연산 반복하면서
for i in range(e):
    # union 연산할 간선 정보 입력받기
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료(주어진 노드들의 루트 노드가 동일하면 사이클이 존재한다는 의미)
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break # 사이클 발견했으니 종료
    # 사이클이 발생하지 않았다면 union 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
