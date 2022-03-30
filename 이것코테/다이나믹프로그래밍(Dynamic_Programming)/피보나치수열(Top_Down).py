# 한 번 계산된 결과를 Memoization 하기 위한 리스트 초기화
# 100까지 만드는 이유는 1~99까지 index로 표현하기 위해
# d[0]은 사용안함
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(Top-Down 방식)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))