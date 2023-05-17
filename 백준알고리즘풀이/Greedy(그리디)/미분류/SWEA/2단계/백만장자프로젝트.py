# 최적화 코드
# 거꾸로 순회하며 계산하는 아이디어
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    max_price = 0
    answer = 0

    for price in prices[::-1]:
        if price >= max_price:
            max_price = price
        else:
            answer += max_price - price

    print("#", test_case, " ", answer, sep="") # 주의 - sep : 각 출력되는 요소의 구분자 지정 가능

#==================================================================
# 내 코드
# 10:00~10:20/10:20~10:50

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # n 입력
    n = int(input())
    # 매매가들 입력(2~1,000,000)
    prices = list(map(int, input().split()))

    # 현재 남은 것 중 최고 매매가 변수
    max_price = max(prices[:])
    # 지금까지 산 금액 합
    buy_price = 0
    # 지금까지 산 개수
    buy_count = 0
    # answer 변수
    answer = 0

    if prices[0] < max_price:
        # 매매가들을 반복하면서
        for i in range(n):
            price = prices[i]
            # 만약 현재 매매가가 최고 매매가보다 작다면
            if price < max_price:
                # 지금까지 산 금액 += 현재매매가
                buy_price += price
                # 지금까지 산 개수 += 1
                buy_count += 1

            # elif 현재 매매가가 최고 매매가와 같다면
            elif price == max_price:
                # answer += 최고매매가 * 지금까지 산 개수 - 지금까지 산 금액 합
                answer += max_price * buy_count - buy_price
                # 남은 매매가 중에서 다시 최고매매가 찾아서 갱신
                if prices[i+1:]:
                    max_price = max(prices[i+1:])
                # 지금까지 산 금액 초기화
                buy_price = 0
                # 지금까지 산 개수 초기화
                buy_count = 0

    # answer 출력
    print(f'#{test_case} {answer}')