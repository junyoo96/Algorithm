# 12:20~

# n : 주어진 숫자
# k : 나누는 수
n, k = map(int, input.split())
result = 0

while True:
    #1. 일일이 1씩 빼지않고 한번에 빼기
    # n == k 로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target) # 1씩 빼는 횟수 더하기
    n = target # 1씩 빼고 남은 나누어떨어지는 숫자

    #2. 나누기 수행
    #N이 K보다 작을 때(더이상 나눌수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1이 될때까지 1씩 빼야되는 횟수 더하기
result += (n-1)

#==========================================================================================
#my code
n, k = map(int, input.split())

result = 0
while n != 1:
    result += 1
    if n % k == 0:
        n //= k
        continue
    n -= 1

print(result)
