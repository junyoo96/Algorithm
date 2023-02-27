import copy

def show(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("==========================")


# 정사각형을 4부분으로 영역 나눠서 회전
arr = [
    [1, 2, 1, 2],
    [4, 3, 4, 3],
    [1, 2, 1, 2],
    [4, 3, 4, 3]
]
length = len(arr)
rotated_arr = copy.deepcopy(arr)

# 정사각형 회전 함수 - 틀림 X
def rotate_square():
    # 여기 구현
    pass

# 영역 1
# 함수 호출
show(rotated_arr)
"""
[4, 1, 1, 2]
[3, 2, 4, 3]
[1, 2, 1, 2]
[4, 3, 4, 3]
"""

# 영역 2
# 함수 호출
show(rotated_arr)
"""
[4, 1, 4, 1]
[3, 2, 3, 2]
[1, 2, 1, 2]
[4, 3, 4, 3]
"""

# 영역 3
# 함수 호출
show(rotated_arr)
"""
[4, 1, 4, 1]
[3, 2, 3, 2]
[4, 1, 1, 2]
[3, 2, 4, 3]
"""

# 영역 4
# 함수 호출
show(rotated_arr)
"""
[4, 1, 4, 1]
[3, 2, 3, 2]
[4, 1, 4, 1]
[3, 2, 3, 2]
"""