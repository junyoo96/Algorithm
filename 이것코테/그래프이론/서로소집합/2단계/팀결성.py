#find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n : 학생 수
# m : 연산 개수
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)
#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

#각 연산을 하나씩 확인
for i in range(m):
    oper, a, b  = map(int, input().split())
    # union 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # find 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")







