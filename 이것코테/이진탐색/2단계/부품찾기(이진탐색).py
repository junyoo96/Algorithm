#이진 탐색 함수 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

# n: 가게의 부품 개수
n = int(input())
# array : 가게에 있는 전체 부품 번호
array = list(map(int, input().split()))
# m : 손님이 확인 요청한 부품 개수
m = int(input())
# array_request : 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
array_request = list(map(int, input().split()))

array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in array_request:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')





