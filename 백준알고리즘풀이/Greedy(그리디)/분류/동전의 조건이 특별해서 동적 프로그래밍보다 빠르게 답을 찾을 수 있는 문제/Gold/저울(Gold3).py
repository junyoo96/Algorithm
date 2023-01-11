# 10:45~11:03 / 11:03~11:13(28분)
# 이것코테의 그리디-만들수없는금액과 동일한 문제

# 저울의 한쪽에는 저울추, 반대쪽에는 무게 측정할 물건
# n : 저울추 개수
    # 무게는 양의정수
# answer : 주어진 무게추를 사용해 측정할 수 없는 양의 정수 무게 중 최솟값 구하기
# 최적해 방안 : 무게종류를 오름차순으로 정렬하여, 작은 무게부터 더하면서 해당 무게가 측정이 가능한지 확인
import sys

# 중요 - 1부터 시작하기
answer = 1
# n 입력
n = int(sys.stdin.readline())
# 무게추 종류 입력
weights = list(map(int, input().split()))
# 무게추 정렬
weights.sort()

# 무게추를 반복하면서
for w in weights:
    # 현재까지의 무게가 현재 무게추 무게보다 작다면
    if answer < w:
        break

    answer += w

# answer 출력
print(answer)