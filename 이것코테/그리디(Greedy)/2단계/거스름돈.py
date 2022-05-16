n = 1260 # 받은 금액
count = 0 # 거슬러줄 동전 개수

coin_types = [500, 100, 50, 10] # 동전 타입 정의

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)