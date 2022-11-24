# 9:30~ / 아이디어 생각 못함

# 직사각형 n(1~50),m(1~50),(적어도 3개의 수)
    # 겹치지 않는 3개의 작은 직사각형으로 나눔
    # 합 : 직사각형속에 있는 수
# answer : 입력으로 주어진 직사각형을 3개 직사각형으로 나눌 때, 각각 작은 직사각형의 합의 곱의 최댓값
#==============================================================
# 답은 최댓값을 출력해야 하므로, 0으로 시작
answer = 0
# 행, 열 입력
n, m = map(int, input().split())
# 입력받은 전체 직사각형을 저장하기 위한 리스트(편리한 인덱싱을 위해 행 삽입)
data = [[0] * (m + 1)]
for _ in range(n):
    # 라인별로 읽고 rectangle_input에 저장(편리한 인덱싱을 위해 [0] 삽입)
    data.append([0] + list(map(int, input())))

# 합을 저장할 리스트
sum_arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 직사각형의 1,1부터 현재 좌표 영역 내 모든 수의 합을 미리 계산해서 해당 좌표 칸에 저장
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 주의 - 빼야되는 부분 좌표 주의
        sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1] + data[i][j]

# 주어진 영역에 속한 수의 합을 계산하는 함수
# x1, y1 : 합을 구하려는 영역의 왼쪽상단 좌표
# x2, y2 : 합을 구하려는 영역의 오른쪽하단 좌표
def sum_area(x1, y1, x2, y2):
    # s[x2][y2] : 직사각형 전체 영역에 속하는 수의 합
    # s[x2][y1 - 1] : 합을 구하려는 영역의 왼쪽 영역에 속하는 수의 합
    # s[x1 - 1][y2] : 합을 구하려는 영역의 위쪽 영역에 속하는 수의 합
    # s[x1 - 1][y1 - 1] : 왼쪽영역과 위쪽영역이 겹치는 영역에 속하는 수의 합
    # 주의 - 빼야되는 부분 좌표 주의
    return sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1]

# 첫 번째 경우: 전체 직사각형을 세로로만 분할한 경우
# O(M^2)
for i in range(1, m - 1):
    for j in range(i + 1, m):
        r1 = sum_area(1, 1, n, i) # 왼쪽 직사각형
        r2 = sum_area(1, i + 1, n, j) # 중간 직사각형
        r3 = sum_area(1, j + 1, n, m) # 오른쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

# 두 번째 경우: 전체 직사각형을 가로로만 분할한 경우
# O(N^2)
for i in range(1, n - 1):
    for j in range(i + 1, n):
        r1 = sum_area(1, 1, i, m) # 위쪽 직사각형
        r2 = sum_area(i + 1, 1, j, m) # 중간 직사각형
        r3 = sum_area(j + 1, 1, n, m) # 아래쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

# 세 번째 경우: 세로 2분할 후 오른쪽 가로로 분할
# O(N*M)
for i in range(1, m):
    for j in range(1, n):
        r1 = sum_area(1, 1, n, i) # 왼쪽 직사각형
        r2 = sum_area(1, i + 1, j, m) # 오른쪽 위쪽 직사각형
        r3 = sum_area(j + 1, i + 1, n, m) # 오른쪽 아래쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

# 네 번째 경우: 세로 2분할 후 왼쪽 가로로 분할
# O(N*M)
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_area(1, 1, i, j) # 왼쪽 위쪽 직사각형
        r2 = sum_area(i + 1, 1, n, j) # 왼쪽 아래쪽 직사각형
        r3 = sum_area(1, j + 1, n, m) # 오른쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

# 다섯번 째 경우: 가로 2분할 후 아래쪽 세로로 분할
# O(N*M)
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_area(1, 1, i, m) # 위쪽 직사각형
        r2 = sum_area(i + 1, 1, n, j) # 아래쪽 왼쪽 직사각형
        r3 = sum_area(i + 1, j + 1, n, m) # 아래쪽 오른쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

# 여섯번 째 경우: 가로 2분할 후 위쪽 세로로 분할
# O(N*M)
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_area(1, 1, i, j) # 위쪽 왼쪽 직사각형
        r2 = sum_area(1, j + 1, i, m) # 위쪽 오른쪽 직사각형
        r3 = sum_area(i + 1, 1, n, m) # 아래쪽 직사각형
        # 만약 각 합의 곱이 현재 최댓값보다 크다면 최댓값 갱신
        answer = max(answer, r1 * r2 * r3)

print(answer)