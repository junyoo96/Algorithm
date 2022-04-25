# #https://www.acmicpc.net/problem/18406
# #3:45~ 4:04
# # 자릿수 문제이기 때문에 리스트 형태로 받아서 풀기
# a = list(map(int, input()))
# digit = len(a) // 2
# # 나뉜 자릿수 기준으로 각 자릿수 숫자들의 합이 동일하다면
# if sum(a[:digit]) == sum(a[digit:]):
#     print("LUCKY")
# else:
#     print("READY")

a = 4321
a = list(map(int,str(a)))
// [4, 3, 2, 1]
print(len(a))
// 4