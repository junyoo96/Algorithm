# 9:11~9:50
# 10:47~11:51
# n : 복도의 크기
# T : 선생님
# S : 학생
# O : 장애물
# X : 빈칸
# 선생님은 상하좌우 방향으로 감시 진행
# 복도에 장애물이 있으면 뒤에 있는 학생을 볼 수 없음

# 3개의 장애물 설치
# 모든 학생이 감시 피할 수 있게

# 출력 - 장애물 설치해서 모든 학생이 선생님의 감시 피할 수 있는지 YES OR NO

#==================================================================================

from itertools import combinations
import copy

answer = 'NO'
# 입력 받기
n = int(input()) # 복도 크기
emptys = []  # 모든 장애물 놓을 수 있는 빈칸 위치 정보
teachers = [] # 모든 선생님 위치 정보
map = [] # 복도 정보

for i in range(n):
    map.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if map[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 빈공간 위치 저장
        elif map[i][j] == 'X':
            emptys.append((i, j))

# 방향 - 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 학생 발견 함수(복도, x, y, 방향, 발견 여부)- DFS 방식으로 재귀로 구현
def find_student(data, x, y, direction, isFound):
    # 만약 현재 위치가 복도에서 벗어났다면(복도끝까지 발견 못했다면) or 현재 위치에 장애물이 있으면
    if (x < 0 or x >= n or y < 0 or y >= n) or (data[x][y] == 'O'):
        return False
    # 만약 학생이 있다면
    elif data[x][y] == 'S':
        return True
        # 학생 발견함수(복도, x+dx[방향], y+ dy[방향], 방향, 발견 여부)
    isFound = find_student(data, x + dx[direction], y + dy[direction], direction, isFound)

    return isFound

# 복도 장애물 중복 조합(순서 상관없이) 3개 생성
obstacle_candidates = combinations(emptys, 3)

# 복도 장애물 조합을 반복하면서
for obstacles in obstacle_candidates:
    # 장애물 설치한 복제 복도 생성
    new_data = copy.deepcopy(map)
    for obstacle in obstacles:
        new_data[obstacle[0]][obstacle[1]] = 'O'
    # 선생님 위치 반복하면서
    isFound = False
    for tx, ty in teachers:
        # 상우하좌 반복하면서
        for i in range(4):
            # 만약 학생을 발견했다면
            if find_student(new_data, tx + dx[i], ty + dy[i], i, False):
                isFound = True
    # 만약 모든 선생님이 감시 했는데 학생을 발견하지 못했다면
    if not isFound:
        answer = 'YES'
        break

print(answer)