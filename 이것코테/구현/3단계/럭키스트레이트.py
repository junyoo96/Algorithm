# #https://www.acmicpc.net/problem/18406
# 3:45~4:04
# 10:12~

# 자릿수 문제이기 때문에 리스트 형태로 받아서 풀기
a = list(map(int, input())) # 주의 - 문자열을 숫자 리스트로 변환 방법
digit = len(a) // 2 # 주의 - / 연산자 사용하면 실수로 계산되는 것
# 나뉜 자릿수 기준으로 각 자릿수 숫자들의 합이 동일하다면
if sum(a[:digit]) == sum(a[digit:]):
    print("LUCKY")
else:
    print("READY")