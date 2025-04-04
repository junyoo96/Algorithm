# 10:00~ 10:10/ 10:10~ - 이진탐색 아이디어 발상 실패

# n : 컴퓨터 개수
# ai : 컴퓨터 성능
    # 성능 d 향상시키는 비용 d^2
    # 업그레이드 안해도 되지만 한 컴퓨터가 두번 이상 업그레이드는 불가
# B : 업그레이드 위한 예산
# answer : B원 이하의 총 비용으로 업그레이드 수행해, 성능이 가장 낮은 컴퓨터의 성능을 최대화할 때 최선의 최저성능 구하기
    # 즉, B의 예산을 이용해 A이상으로 만들 수 있는 가장 큰 자연수 A의 값(가장 낮은 컴퓨터 성능)을 알고리즘을 활용해 찾아내는 문제

# 이진탐색 사용하여 해결
    # 2 x 10^9 ~ 성능이 가장 낮은 컴퓨터의 성능이 1이 될때까지 가능한 모든 성능에 대해서 반복해야하므로, 완전탐색으로는 탐색해야할 개수가 너무 많음
    # 따라서, 이진탐색 문제를 사용해 해결
# ========================
n, b = map(int, input().split())
num_list = list(map(int, input().split()))
# key: 성능, value : 해당 성능을 가지는 컴퓨터 개수
num_dict = {}
# 내림차순으로 정렬
num_list = sorted(num_list, reverse=True)
# 성능중에 제일 작은 성능
left = num_list[-1]
# 최대 숫자(2 * 10^9) -> 10^9는 컴퓨터성능의 범위
right = 2000000000

# 성능을 반복하면서 성능별로 컴퓨터개수 저장
for i in num_list:
    if i not in num_dict.keys():
        num_dict[i] = 1
    else:
        num_dict[i] += 1

# mid : 원하는 최적의 값(예산내에서 성능이 가장 낮은 컴퓨터 성능의 최대 성능)
# left는 업그레이드 비용이 절대로 B를 넘지 않음
# right는 업그레이드 비용이 절대로 B 아래가 되지 않음
# 때문에 right-left=1 이라는 것은 B를 넘지 않는 최대 효율이 left라는 것
while right - left > 1:
    mid = (right + left) // 2
    cur_cost = 0
    # mid를 left또는 right 어느쪽에 갱신할지 여부를 저장하는 변수
    isLeft = 1
    # 성능별 컴퓨터 개수를 가진 딕션너리를 반복하면서(성능, 해당 성능 컴퓨터 개수)
    for k, v in num_dict.items():
        # 만약 컴퓨터 성능이 현재 성능보다 작은 경우라면 업그레이드 해야됨
        if k < mid:
            # 컴퓨터 성능을 현재 성능으로 업그레이드 하기 위해 필요한 비용을 계산해 업그레이드 비용 계산
            cur_cost += ((mid - k) ** 2) * v
            # 만약 업그레이드 비용이 예산을 초과한다면
            if cur_cost > b:
                # 더 낮은 성능으로 업그레이드 하기 위해 mid값 변경
                right = mid
                isLeft = 0
                # 현재 성능으로 업그레이드 하지는 못하기 때문에 이진탐색 다시 하기위해 for문 종료
                break
    # 업그레이드 비용이 예산을 초과하지 않았기 때문에 원래 업그레이드할 성능보다 더 높여서 가장 낮은 컴퓨터 성능을 업그레이드 하기 위해
    if isLeft:
        left = mid
print(left)