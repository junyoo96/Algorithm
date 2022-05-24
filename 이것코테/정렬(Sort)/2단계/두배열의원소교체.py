n, k = map(int, input.split())
a = list(map(int, input.split()))
b = list(map(int, input.split()))

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #A의 원소가 B의 원소보다 작은 경우만 스왑
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# 배열 A의 모든 원소의 합 출력
print(sum(a))