# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        # 값이 x인 원소의 개수는 0개이므로 0 반환
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if array[mid] == target and (mid == 0 or array[mid - 1] < target):
        return mid
    # 위의 조건에 맞지 않는 것 중에서 현재 값이 target보다 크거나 같은 경우
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 현재값이 찾고자 하는 값보다 작은 경우
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if array[mid] == target and (mid == n - 1 or array[mid + 1] > target):
        return mid
    # 현재값이 찾고자 하는 값보다 큰 경우
    elif array[mid] > target:
        return first(array, x, start, mid - 1)
    # 현재값이 찾고자 하는 값보다 작거나 같은 경우
    else:
        return first(array, x, start, mid + 1)

# n : 데이터 개수
# x : 찾고자 하는 숫자
n, x = map(int, input().split())
# 전체 숫자 데이터 입력받기
array = list(map(int, input().split()))

# 값이 x인 데이터의 개수 계산
count = count_by_value(array, x)
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)


#=========================================================================
#내가 푼것
#12:25~ 12:55
# 이진 탐색 함수(array, target, start, end, cnt)
def binary_search(array, target, start, end, cnt):
    # 만약 start가 end보다 크다면
    if start > end:
        return -1
    mid = (start + end) // 2
    # 만약 target이 array[mid]과 같다면
    if target == array[mid]:
        # 양옆으로 체크해서 숫자 몇개있는지 확인하기
        # 이전 확인
        i = mid - 1
        while array[i] == target and i >= 0:
            cnt += 1
            i -= 1
        # 이후 확인
        i = mid
        while array[i] == target and i < n:
            cnt += 1
            i += 1

        return cnt
    # 만약 target이 array[mid]보다 작다면
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1, cnt)
    # 만약 target이 array[mid]보다 크다면
    else:
        return binary_search(array, target, mid + 1, end, cnt)

n, target = list(map(int, input().split()))
numbers = list(map(int, input().split()))

cnt = 0
answer = binary_search(numbers, target, 0, n - 1, cnt)

print(answer)

