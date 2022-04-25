# 1:36~

# 2차원 리스트 90도 회전 함수
def rotate_a_matrix_by_90_degree(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)] # key 원본인 훼손안되게 크기가 같은 이중 리스트 생성
    #회전식(암기)
    for i in range(n): # 행
        for j in range(m): # 열
            result[j][n - i - 1] = key[i][j] # 암기
    return result

# 확장된 자물쇠의 중간 부분(원래 자물쇠 부분)이 모두 1인지(열쇠로 자물쇠가 열리는지) 확인하는 함수
def check(new_lock):
    lock_length = len(new_lock) // 3
    #자물쇠 부분이 모두 1인지 확인하기
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock) # 자물쇠의 크기
    m = len(key) # 열쇠의 크기

    # 1. 자물쇠의 크기를 기존의 3배로 변경
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 2. 4가지 회전 경우에 대해서 확인
    for rotation in range(4):
        # 3. 열쇠 회전
        key = rotate_a_matrix_by_90_degree(key)
        # 자물쇠에 열쇠를 끼워 넣기
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 4. 새로운 자물쇠에 열쇠가 정확히 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 5. 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False

key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
print(solution(key, lock))