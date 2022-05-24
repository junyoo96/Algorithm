n = int(input())
array = list(map(int, input.split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d= [0] * 100

# 다이나믹 프로그래밍 진행(Bottom-Up 방식)
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2, n):
    # (현재 창고 식량 + 2칸 왼쪽에 있는 창고 식량) vs (1칸 왼쪽에 있는 창고 식량만, 현재창고실량은 못털고) 를 비교해서
    # 더 많은 식량을 터는 방법 고르는 것
    d[i] = max(d[i-1], d[i-2] + array[i])

# DP테이블 마지막칸에 계산해 얻을 수 있는 식량의 최댓값이 계산되어 있음
# 계산된 얻을 수 있는 식량의 최댓값 출력
print(d[n-1])

