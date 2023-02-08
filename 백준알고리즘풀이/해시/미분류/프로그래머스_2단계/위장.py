# 12:06~12:37/12:43~1:15

# 의상(1~30)
# 의상이름, 의상종류
# 문자열로 이루어져 있음(1~20)
# 같은 이름을 가진 의상은 존재하지 않음
# 하루에 최소한 한개의 의상은 입음
# answer : 서로 다른 옷의 조합수
# =========================================
from collections import defaultdict

def solution(clothes):
    answer = 1

    # 각 옷종류 개수 계산
    count = defaultdict(lambda: 0)
    for cloth in clothes:
        count[cloth[1]] += 1

    # 경우의 수 계산
    for value in count.values():
        # 해당 옷 종류를 안입는 경우의 수도 있으니까 + 1해서 곱하기
        answer *= value + 1

    # 모든 종류를 아예 안 입는 경우의수는 빼기
    answer -= 1

    return answer