# 10:45~10:55 / 10:55~10:58(13분)

# n : 정사각형 공간 크기
# 상하좌우로 이동 가능
    # 시작 좌표는 항상 1,1
    # n,n의 공간을 벗어나는 움직임은 무시됨

# 계획서
    # L : 왼쪽이동
    # R : 오른쪽 이동
    # U : 위로 이동
    # D : 아래로 이동
# answer : 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표 출력
#===============================================================================
import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# 방향 그래프 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 여행 계획 입력
plans = list(input().split())
# 현재 위치
x = 0
y = 0
# 이동 종류
move_types = ['U', 'R', 'D', "L"]

# 여행 계획 입력을 반복하면서
for p in plans:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 만약 이동한 좌표가 올바른 범위안에 있다면
    if 0 <= nx < n and 0 <= ny < n:
        # 현재 좌표를 이동한 좌표로 갱신
        x = nx
        y = ny

# 현재좌표에서 각각 +1 한것을 출력
print(x + 1, y + 1)