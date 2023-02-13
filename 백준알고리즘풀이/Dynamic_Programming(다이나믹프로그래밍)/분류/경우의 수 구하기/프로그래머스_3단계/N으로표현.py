#11:00~ / 아이디어 생각 못함
# answer : N과 사칙연산만 사용해서 표현할 수 있는 방법 중 N 사용횟수의 최솟값 반환
# 최적화 코드
def solution(N, number):

    # 만약 숫자가 한개 라면
    if number == 1:
        return 1

    # 중요 - 주어진 숫자를 사용하는 횟수별로 만들 수 있는 수의 집합 저장
    set_list = []
    # 1개부터 8개까지 확인 - 숫자를 사용하는 최소 횟수가 8보다 크면 무조건 -1 반환함으로 8까지만 확인
    for cnt in range(1, 9):
        # 중요 - 현재 횟수만큼 사용해서 만들 수 있는 수의 집합 저장
        partial_set = set()
        # 1. 이어 붙이기만 해서 만드는 경우 추가
        partial_set.add(int(str(N) * cnt))

        # (1, n-1) 부터 (n-1, 1)까지 사칙연산
        # 예를 들어 숫자를 5번 사용하는 수집합을 구하는 경우라면, 다음과 같은 수집합 경우의 수를 계산
            # 1번 사용하는 수집합 , 4번 사용하는 수집합에 대한 사칙연산을 통해 얻을 수 있는 수집합
            # 2번 사용하는 수집합 , 3번 사용하는 수집합에 대한 사칙연산을 통해 얻을 수 있는 수집합
            # 3번 사용하는 수집합 , 2번 사용하는 수집합에 대한 사칙연산을 통해 얻을 수 있는 수집합
            # 4번 사용하는 수집합 , 1번 사용하는 수집합에 대한 사칙연산을 통해 얻을 수 있는 수집합
        for i in range(cnt - 1):
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2) # 2. +
                    partial_set.add(op1 * op2) # 3. *
                    partial_set.add(op1 - op2) # 4. -
                    # 만약 분모가 0이 아니면
                    if op2 != 0:
                        partial_set.add(op1 / op2) # 5. /
        # 만약 만든 수 집합에 만들려고 하는 타겟숫자가 있다면
        if number in partial_set:
            # 현재 사용 횟수 반환
            return cnt
        # 횟수별 수 집합 저장하는 것에 현재 수 집합 추가
        set_list.append(partial_set)

    # 8번까지도 찾을려는 타겟숫자륾 만들 수 없는 경우 -1 반환
    return -1