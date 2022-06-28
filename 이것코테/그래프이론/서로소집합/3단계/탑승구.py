#9:53~

# g : 탑승구 개수
    # 다른 비행기가 도킹하지 않은 탑승구에만 도킹 가능
    # 도킹할 수 없는 비행기가 나오는 경우 공행 운행 중지
# p : 비행기 개수

# answer : 최대 도킹할 수 있는 비행기 개수

# 도킹가능한 탑승구가 적은 비행기부터 배치하기

# 서로소 집합 알고리즘으로 풀기

# find 함수
def find_parent(parent, x):
    if x != parent[x]:
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
g = int(input())
p = int(input())

# 부모 테이블 초기화
parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i

for _ in range(p):
    # 가능한 탑승구 중 가장 큰 수를 입력받아서 해당 노드의 루트 노드 구하기
    data = find_parent(parent, int(input()))
    # 만약 현재 노드의 루트노드가 0 이라면
    if data == 0:
        break
    # 만약 그렇지 않다면 왼쪽 노드와 union 연산
    union_parent(parent, data, data - 1)
    # 도킹가능한 비행기 개수 증가
    answer += 1

# 답 출력
print(answer)
