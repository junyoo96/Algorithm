def rotate_matrix_by_90_degree(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = key[i][j]

    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    # n : key의 크기
    n = len(key)
    # m : lock의 크기
    m = len(lock)

    # 자물쇠 부분을 3배로 키우기
    new_lock = [[0] * (m*3) for _ in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_lock[i + m][j + m] = lock[i][j]

    # for - key를 4가지 회전 방향에 대해서 자물쇠에 맞는지 반복하면서
    for a in range(4):
        # func - 회전한 key 구하는 함수
        key = rotate_matrix_by_90_degree(key)

        for x in range(m*2):
            for y in range(m*2):
                # key를 이동하는 것을 반복하면서
                for i in range(n):
                    for j in range(n):
                        # ? 3x3 으로 예를 든다면, 왜 i+x의 마지막이 8이 아니라 7이지
                        new_lock[i + x][j + y] += key[i][j]
                #함수 - 열쇠가 자물쇠에 맞는지 확인
                if check(new_lock) == True:
                    return True
                # 맞으면 return True
                for i in range(n):
                    for j in range(n):
                        new_lock[i + x][j + y] -= key[i][j]
            #아닌 경우에 new_lock에 자물쇠 빼기
    return False