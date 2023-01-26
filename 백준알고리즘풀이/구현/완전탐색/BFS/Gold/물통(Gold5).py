# 9:20~ / 아이디어 생각 못함
# 9:55~10:21 / 10:21~10:55

# answer : A물통이 비어있을 때, C물통에 담겨있는 물의 양의 종류를 모두 구하기
#=================================================================================================
# 최적화 코드
import sys
from collections import deque

def pour(x, y):
    if not visited[x][y]:
        # 방문처리
        visited[x][y] = True
        # # a 물통과 b 물통의 경우의 수 저장
        queue.append((x, y))

def bfs():
    while queue:
        # a1 : 현재 남아있는 a 물통의 물의 양, b1 : 현재 남아있는 b 물통의 물의 양, c1 : 현재 남아있는 c 물통의 물의 양
        a1, b1 = queue.popleft()

        # c물통에 남아있는 물의 양
            # 처음 시작할때 c물통에 모든 물이 있으므로,
                # c(처음 c물통의 물의양)에서 a1(현재 a물통의 물의 양)과 b1(현재 b물통의 물의양)을 빼면, c1(현재 c물통에 남아있는 물의양)을 알 수 있음
        c1 = c - a1 - b1

        # 현재 a 물통이 비어있는 경우 현재 c 물통에 남아있는 물의 양 저장
        if a1 == 0:
            answer.append(c1)

        # 물을 옮길 수 있는 경우의 수 6가지
        # 1. a -> b
        # 중요 - water : a 물통에서 b 물통으로 들어 갈 수 있는 물의 양 체크
            # min(현재 a물통의 물의양, b물통에 b물통 용량 - 현재 b물통에 들어있는 물의양)
            # = min(현재 a물통의 물의양, b물통에 남아있는 공간)
            # 즉, a에서 b로 옮길 때,
                # b물통에 남아있는 공간 > a물통의 물의양 -> b물통에 남아있는 공간만큼의 물만 a물통에서 b물통으로 물을 옮길 수 있음
                # b물통에 남아있는 공간보다 a물통의 물의양이 적은 경우 -> a물통에 물의양 전체를 a물통에서 b물통으로 물을 옮길 수 있음
        water = min(a1, b - b1)
        # 체크한 물 양을 a 물통에서 빼주고 b 물통에 넣어 경우의 수 탐색
        pour(a1 - water, b1 + water)

        # 2. a -> c
        # a 물통에서 c 물통으로 들어 갈 수 있는 물의 양 체크
        water = min(a1, c - c1)
        # 체크한 물 양을 a 물통에서 빼주고 경우의 수 탐색
        pour(a1 - water, b1)

        # 3. b -> a
        # b 물통에서 a 물통으로 들어 갈 수 있는 물의 양 체크
        water = min(b1, a - a1)
        # 체크한 물 양을 b 물통에서 빼주고 a 물통에 넣어 경우의 수 탐색
        pour(a1 + water, b1 - water)

        # 4. b -> c
        # b 물통에서 c 물통으로 들어 갈 수 있는 물의 양 체크
        water = min(b1, c - c1)
        # 체크한 물 양을 b 물통에서 빼주고 경우의 수 탐색
        pour(a1, b1 - water)

        # 5. c -> a
        # c 물통에서 a 물통으로 들어 갈 수 있는 물의 양 체크
        water = min(c1, a - a1)
        # 체크한 물 양을 b 물통에서 빼주고 경우의 수 탐색
        pour(a1 + water, b1)

        # 6. c -> b
        # c 물통에서 b 물통으로 들어 갈 수 있는 물의 양 체크
        water = min(c1, b - b1)
        # 체크한 물 양을 b 물통에서 빼주고 경우의 수 탐색
        pour(a1, b1 + water)

# answer : a 물통의 양이 0일 때 c 물통의 양의 종류
answer = []

# 각 통의 부피
a, b, c = map(int, sys.stdin.readline().split())

queue = deque()
# a 물통과 b 물통의 물의 양이 0일때(아무것도 안옮길 때부터)부터 탐색
queue.append((0, 0))

# 2차원 방문 여부 리스트(통의 부피 범위가 1~200이므로 201로 설정)
visited = [[False] * 201 for _ in range(201)]
# (0,0)일 때 방문처리
visited[0][0] = True

bfs()

# 오름차순 정렬 후 출력
answer.sort()
# * : 리스트를 공백 간격 출력으로 처리
print(*answer)
#=====================================================================
# 2번째 풀이에서 성공한 내 코드
# 9:55~10:21 /10:21~10:55

# A, B, C 물통(1~200)
# A, B는 비어있음
# C는 가득차 있음
# 한 물통이 비거나 다른 한 물통이 가득찰 때까지 물을 부을 수 있음
# answer : A통이 비어있을 때, C 물통에 담겨 있을 수 있는 물의 양 모두 구하기, 용량 오름차순 정렬

# =========================
from collections import deque

# 물통 크기 리스트(a,b,c)
bottle_size = list(map(int, input().split()))
# deque에 현재 상태 추가
queue = deque()
queue.append([0, 0, bottle_size[2]])
# visited 리스트 생성
visited = []
visited.append([0, 0, bottle_size[2]])

# answer 변수(set)
answer = []
# while queue
while queue:
    # 물통리스트 = deque에서 꺼내기
    bottles = queue.popleft()

    # 만약 현재 a 물통(물통리스트 첫번째)이 0이라면
    if bottles[0] == 0:
        # answer에 추가
        answer.append(bottles[2])

    # 3번 반복하면서 - 시작물통
    for i in range(3):
        # 3번 반복하면서 - 타겟물통
        for j in range(3):
            bottles_tmp = bottles[:]
            # 만약 현재 시작물통의 물이 타겟물통과 같지 않다면
            if i != j:
                # 물 붓는 것 처리
                # 만약 현재 타겟물통의 양 + 시작물통의 양이 타겟물통크기보다 작거나 같다면
                if bottles_tmp[j] + bottles_tmp[i] <= bottle_size[j]:
                    # 타겟물통의양 = 타겟물통의 양 + 시작물통의 양
                    bottles_tmp[j] += bottles_tmp[i]
                    # 시작물통의양 = 0
                    bottles_tmp[i] = 0
                # else
                else:
                    # 시작물통의양 = 타겟물통의 양 + 시작물통의양 - 타겟물통크기
                    bottles_tmp[i] = bottles_tmp[j] + bottles_tmp[i] - bottle_size[j]
                    # 타겟물통의양 = 타겟물통크기
                    bottles_tmp[j] = bottle_size[j]

                # 현재 상태가 visited리스트에 없다면
                if bottles_tmp not in visited:
                    # deque에 추가
                    queue.append(bottles_tmp)
                    # visited리스트에 현재 상태 추가
                    visited.append(bottles_tmp)

# answer 출력
answer.sort()
print(*answer)



