# 11:50~12:05 / 12:05~12:15

# m : 필요한 나무 길이(1~20억)
# 목재절단기
# H : 절단기에 높이 지정
# 절단기 위에 있는 나무 길이만 가져갈 수 있음
# n : 나무개수(1~백만)
# 상근이는 집에 필요한 나무를 항상 가져갈 수 있음
# answer : 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값
# =======================================
import sys
input = sys.stdin.readline

# n,m 입력
n, m = map(int, input().split())
# 나무의 높이 주어짐(0~10억)
trees = list(map(int, input().split()))

# 이분탐색 함수(필요한 나무길이, 시작범위, 끝범위) # O(logN)
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 주어진 나무들을 현재 절단기 높이로 자르면서 얻을 수 있는 나무 길이 계산
        value = 0
        for tree in trees:  # O(N)
            # 중요 - 이거없으면 시간초과남, 절단기 높이보다 높은 나무만 계산하면서 연산 줄여서 시간초과 해결가능(Pypy3안쓰고 Python3로 돌려도 시간초과 안남)
            if tree >= mid:
                value += tree - mid

        # 만약 계산한 나무길이가 필요한 나무길이보다 크거나 같다면
        if value >= target:
            # 필요한 나무길이를 충족하면서 절단기 높이를 최대로 하고 싶음으로 시작범위 증가
            start = mid + 1
        else:
            # 얻어갈 나무가 없으므로 끝범위 감소
            end = mid - 1

    return end

# answer = 이분탐색 함수 호출(필요한 나무 길이, 1, 주어진 나무 높이중 가장 큰 나무 높이)
answer = binary_search(m, 1, max(trees))
# answer 출력
print(answer)