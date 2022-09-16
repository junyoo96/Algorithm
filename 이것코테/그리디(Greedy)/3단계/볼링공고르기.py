# 9:40~9:55
# 풀긴했는데 다른 방법 생각 못함)

# n: 볼링공 수
# 1~m: 볼링공 무게 최대
# 두 사람이 볼링공을 고르는 경우의 수
    # 서로 무게가 다른 볼링공 골라야함

# answer - 두 사람이 볼링공을 고르는 경우의 수
#=================================================================================
answer = 0

n, m = map(int, input().split())
weights = list(map(int, input().split()))

array = [0] * 11 # 1~10까지의 무게를 담을 수 있는 리스트

for weight in weights:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[weight] += 1

# 1부터 m까지의 각 무게에 대해 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    answer += array[i] * n # A가 선택할 수 있는 개수 * B가 선택하는 경우의 수를 곱해서 전체 경우의 수 더하기

print(answer)
#=================================================================================
# answer = 0
#
# n, m = map(int, input().split())
# weights = list(map(int, input().split()))
#
# # 볼링공 무게대로 오름차순 정렬
#
# # 볼링공 무게 리스트 반복하면서
# for i in range(len(weights)):
#     for j in range(i + 1, len(weights)):
#         # 만약 현재 무게와 다르다면
#         if weights[i] != weights[j]:
#             # answer 증가
#             answer += 1
#
# print(answer)
