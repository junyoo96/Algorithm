# 10:31~10:40 / 10:40~ - 틀림

# 정수값 범위 : 정수 범위 -2^31~2^31(21억 4천..)
# answer : 존재하면 1, 않으면 0 출력
# 탐색 범위가 매우 넓음므로 이진 탐색 사용해야함
# ===================
# 원소개수 n 입력(1~100,000)
n = int(input())
# n개의 정수를 입력
sources = list(map(int, input().split()))
sources.sort() # 주의 - 이분탐색할 리스트가 정렬이 안된 경우 먼저 정렬해야함
# 원소 개수 m 입력(1~100,000)
m = int(input())
# m개의 수들을 입력
targets = list(map(int, input().split()))


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if sources[mid] == target:
            return True
        elif sources[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False

# m개의 수를 반복하면서
for target in targets:
    # 만약 해당 수가 존재한다면
    if binary_search(target, 0, n - 1):
        # 1 출력
        print(1)
    # else
    else:
        # 0 출력
        print(0)