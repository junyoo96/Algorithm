# 빈칸 이중 리스트 생성 (3*3짜리 빈칸 이중리스트 생성하기)
n = 3
list = [
    [[] for _ in range(n)]
    for _ in range(n)
]

print(list)
