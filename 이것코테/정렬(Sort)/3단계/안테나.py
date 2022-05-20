# 1:50~
answer = 0

n = int(input())
houses = list(map(int, input().split()))
# 집 위치 리스트 오름 차순 정렬
houses.sort()

# 중간값(median) 출력
print(houses[(n - 1) // 2])