# 12:56~
# 틀림

n = int(input())
coins = list(map(int, input().split()))
coins.sort() # 동전 오름차순 정렬

# 현재 상태를 1 ~ target-1 까지의 모든 금액을 만들 수 있는 상태라 가정

# 만들고자 하는 금액을 1원부터 시작
# target이 의미하는 것은 현재까지 주어진 동전으로 만들수 있는 금액의 + 1 된 것
    # target까지는 주어진 동전의 조합으로 모두 만들 수 있는 것이 보장됨
# 따라서 새로 주어지는 coin이 target보다 크다면 target에 해당하는 금액을 만들 수 없게됨
target = 1
for coin in coins:
    # 매번 target인 금액도 만들 수 있는지 체크하기
        # 현재 코인이 만들고자 하는 금액보다 클 경우, 만들고자 하는 금액을 만드는 방법은 없기 때문에, 해당 금액이 만들 수 없는 최소 금액이 됨
    if target < coin:
        break
    # 해당 금액을 만들 수 있다면, target의 값을 업데이트
        # 현재 코인 만들고자 하는 금액보다 적은 경우, ((만들고자 하는 금액 + 현재 코인) - 1)의 금액 까지 만들 수 있다는 의미가 되기 때문에 만들고자 하는 금액을 높임
    target += coin

print(target)

#========================================================================
# from itertools import combinations # 주의 - itertools.combinations
#
# answer = 0
#
# n = int(input())
# coins = list(map(int, input().split()))
# # 동전 리스트 오름차순 정렬
# coins.sort()
#
# # 함수
# # 조합 라이브러리 푸는 문제 선택 개수 늘려가면서 - 완전탐색
# def check_possible(money):
#     for i in range(1, n + 1):
#         for candidate in combinations(coins, i):
#             if sum(list(candidate)) == money:
#                 return True
#     return False
#
# # 1원부터 1,000,000 * n 까지 반복하면서
# for i in range(1, coins[-1] * n):
#     # 함수 - 동전 리스트로 조합해서 현재 금액 만들 수 없다면
#     if not check_possible(i):
#         answer = i
#         break
#
# # 현재 최소 금액 출력
# print(answer)