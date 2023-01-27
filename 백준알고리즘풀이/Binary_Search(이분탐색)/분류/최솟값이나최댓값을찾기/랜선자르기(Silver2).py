# n : 캠프 때 쓸 랜선 개수(1, 백만)
# k : 오영식이 갖고있는 랜선 개수(1~10,000)
# 길이가 제각각(랜선의 길이는 2^31 - 1보다 작거나 같은 자연수)
# 랜선을 모두 N개의 같은 길이 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야함
# 기존 K의 랜선으로 N개의 랜선을 무조건 만들 수 있음
# 자를 때는 항상 센티미터 단위로 정수길이 만큼 자름
# N개보다 많이 만드는 것도 N개에 포함됨
# answer : 만들 수 있는 최대 랜선의 길이

# 탐색범위인 랜선의 길이 범위가 (1~2^31)까지 이므로 이분탐색 사용
# ===================================
# 최적화 코드
# k,n 입력
k, n = map(int, input().split())
# k만큼 반복하면서 갖고있는 랜선의 길이 입력
lines = [int(input()) for _ in range(k)]

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 현재 길이로 오영식이 갖고 있는 랜선들을 잘라서 얻은 랜선 개수
        count = 0
        for line in lines:
            count += line // mid

        # 만약 필요한 랜선개수(n)보다 잘라서 얻은 랜선 개수가 크거나 같다면
        if count >= target:
            # 자를 길이를 더 늘려도 되므로 시작범위 증가
            start = mid + 1
        else:
            # 자를 길이를 줄어야 되므로 끝범위 감소
            end = mid - 1

    # 중요 - 이분탐색 하다보면 결국 start와 end가 만나는 지점이 랜선의 최대길이가 되므로 end를 반환
    return end

# 중요 - 이분탐색 범위 (1~ 오영식이 갖고 있는 랜선 중 최대길이)
    # 최대 길이이상으로 자르게 되면 아무것도 못자르기 때문에 최대 범위로 지정됨
answer = binary_search(n, 1, max(lines))
print(answer)

#=====================================
# 내코드
# 12:55~1:10/ 1:10~1:25

# k,n 입력
k, n = map(int, input().split())
# k만큼 반복하면서 갖고있는 랜선의 길이 입력
lines = [int(input()) for _ in range(k)]


# 이분탐색 함수(필요한 랜선의 개수 , 시작범위, 끝범위)
def binary_search(target, start, end):
    # 최대길이 변수
    max_val = 0
    # while start <= end
    while start <= end:
        mid = (start + end) // 2
        # 현재길이로 갖고있는 랜선 나누기
        count = 0
        for line in lines:
            count += line // mid

        # 만약 현재 길이로 갖고있는 랜선들을 나눴을 때 몫이 필요한 랜선 개수 보다 크다면
        if count >= target:
            # max 갱신
            max_val = max(max_val, mid)
            # start = mid + 1
            start = mid + 1
        # else
        else:
            # end = mid - 1
            end = mid - 1
    # return 최대 길이
    return max_val


# answer = 이분탐색함수(target은 n보다 같거나 큰 경우, 1, 2^31)
answer = binary_search(n, 1, 2 ** 31 - 1)
# answer 출력
print(answer)