#10:58~
# n : 화폐 종류
# m : 최종적으로 만드려는 가치의 합
n, m = map(int, input.split())

coin_type = []
for i in range(n):
    coin_type.append(int(input.split()))

d = [10001] * (m+1)
d[0] = 0

# 화폐 종류 만큼 반복
for i in range(n):
    # 현재 화폐 종류 금액 부터 끝까지
    for j in range(coin_type[i], m + 1):
        if d[j-coin_type[i]] != 10001 : # (i-k)원을 만드는 방법이 존재하는 경우 , ex) 현재 최소횟수를 찾으려는 값이 5원 이고 화폐 종류가 2,3원일 때 (5-2)를 만드는방법이 존재하는 경우
            # 점화식, 둘중에 최소 횟수구하기(현재까지 저장된 최소 횟수 or 이전 동전까지의 최소횟수 + 1)
            # +1 하는 이유는 이전 동전횟수에 동전을 더하는 거니까 횟수 하나 더하는것
            d[j] = min(d[j], d[j-coin_type[i]] + 1)

    # 계산된 결과 출력
    if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
        print(-1)
    else:
        print(d[m])