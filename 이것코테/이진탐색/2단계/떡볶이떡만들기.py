# n : 떡 개수
# m : 손님이 요청한 떡 길이
n, m = map(int, input().split())
# 각 떡의 개별 길이 정보
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
# 최대의 mid값(절단기에 설정할 수 있는 높이의 최대값)을 찾는 과정
while start <= end:
    total = 0
    mid = (start+end) // 2
    # 잘랐을 때의 떡 양 계산
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid # 절단기에 설정할 수 있는 높이의 최대값(최대한 떡이 덜 잘리는 것)을 구함으로
        start = mid + 1

print(result)


