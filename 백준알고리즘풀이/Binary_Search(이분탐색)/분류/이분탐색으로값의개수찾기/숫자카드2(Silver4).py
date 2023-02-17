# 11:18~11: / - 틀림(숫자찾았을 때 주변 숫자찾기에서 시간초과남)

# n : 숫자 카드 개수(1~500,000)
# 적혀있는 숫자(-천만 ~ 천만)
# m : 주어지는 숫자 개수(1~500,000)
# 적혀있는 숫자(-천만 ~ 천만)
# answer : 각 수가 적힌 숫자 카드를 상근이가 몇개 가지고 있는지 공백으로 구분해 출력
# ==================================
import sys

input = sys.stdin.readline

# n 입력
n = int(input())
# n만큼 숫자 카드 입력
sources = list(map(int, input().split()))
sources.sort()
# m 입력
m = int(input())
# m만큼 숫자 입력
targets = list(map(int, input().split()))

# 이분탐색 함수(타겟숫자, 시작위치, 끝위치)
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if sources[mid] == target:
            # 중요 - 이분탐색으로 값이 존재하는지 파악한뒤에는 타겟숫자에 대해 count함수로 몇개존재하는 탐색
            return sources[start:end + 1].count(target)
        elif sources[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

# m 숫자를 반복하면서
dic = {}
for target in targets:
    if target not in dic: # 중요, 주의 - 이거없으면 시간초과남, dictionary 사용해서 해당값을 이미 찾았다면 binary_search 진행을 진행하지 않으므로써, 시간 초과 해결 가능
        # answer = 이분탐색 함수호출(m, 시작위치, 끝위치)
        dic[target] = binary_search(target, 0, n - 1)

# 공백을 통해 한줄로 출력
print(' '.join(str(dic[x]) if x in dic else '0' for x in targets))

#========================================================================
# 내코드 - defaultdict 사용
# 11:18~11:19 / 11:19~11:23 - 맞음

# n : 숫자 카드 개수(1~500,000)
# 적혀있는 숫자(-천만 ~ 천만)
# m : 주어지는 숫자 개수(1~500,000)
# 적혀있는 숫자(-천만 ~ 천만)
# answer : 각 수가 적힌 숫자 카드를 상근이가 몇개 가지고 있는지 공백으로 구분해 출력
# ==================================
from collections import defaultdict
import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# n만큼 숫자 카드 입력
sources = defaultdict(lambda: 0)
for i in list(map(int, input().split())):
    sources[i] += 1

# m 입력
m = int(input())
# m만큼 숫자 입력
targets = list(map(int, input().split()))
for target in targets:
    print(sources[target], end = ' ')