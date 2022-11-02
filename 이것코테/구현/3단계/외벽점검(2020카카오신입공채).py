# 아이디어 생각 못함
# 12:00~ / 아이디어 생각 못함
# ============================================================
from itertools import permutations


def solution(n, weak, dist):
    # 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값
    answer = 0

    # n : 외벽의 총 둘레
    # weak : 취약 지점의 위치가 담긴 배열 (시계 형식)
    # dist : 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열

    length = len(weak)  # 취약 지점의 개수
    # 주의 - 길이를 2배로 늘려서 원형을 일자 형태로 변형
    for i in range(length):
        # 취약 지점 위치에 외벽의 총 둘레를 더해주어 추가하기
        weak.append(weak[i] + n)
    # 주의 - 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # len(dist) : 투입가능한 최대 친구의 수 를 의미
    answer = len(dist) + 1

    # 취약 지점의 시작점을 반복하면서(점검을 어느 취약지점부터 시작할지)
    for start in range(length):
        # 친구들의 조합을 반복하면서 (어떤 거리를 가진 친구가 취약점검을 하러 갈지에 대한 순서)
        for friends in permutations(dist, len(dist)):
            count = 1  # 투입할 친구의 수
            position = weak[start] + friends[count - 1]  # 해당 친구가 점검할 수 있는 마지막 위치
            # 시작점부터 모든 취약 지점을 확인(취약 지점 개수만큼 반복하면서)

            # 취약 지점을 반복하면서(점검 시작한 위치부터 시작)
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우(현재 친구가 목표 취약 위치까지 도달 할 수 없는 경우)
                if position < weak[index]:
                    # 새로운 친구를 투입
                    count += 1
                    # 더 친구 투입이 불가능하다면 종료
                    if count > len(dist):
                        break

                    # 해당 친구가 점검할 수 있는 마지막 위치
                    position = weak[index] + friends[count - 1]

            # 투입한 친구 최소값 계산
            answer = min(answer, count)
    # 투입해야되는 친구가 존재하는 친구보다 많은 경우
    if answer > len(dist):
        return -1
    return answer


print("==================================================")
print("답", solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

# =====================================================================================

# 디버깅용 코드
# 친구들의 순열을 생성하기 위해 사용
from itertools import permutations


def solution(n, weak, dist):
    # 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값
    answer = 0

    # n : 외벽의 총 둘레
    # weak : 취약 지점의 위치가 담긴 배열 (시계 형식)
    # dist : 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열

    length = len(weak)  # 취약 지점의 개수
    # 주의 - 길이를 2배로 늘려서 원형을 일자 형태로 변형
    for i in range(length):
        # 취약 지점 위치에 외벽의 총 둘레를 더해주어 추가하기
        weak.append(weak[i] + n)
    # 주의 - 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # len(dist) : 투입가능한 최대 친구의 수 를 의미
    answer = len(dist) + 1

    print("length", length)
    print("weak", weak)
    print("================")

    # 취약 지점의 시작점을 반복하면서(점검을 어느 취약지점부터 시작할지)
    for start in range(length):
        # 친구들의 조합을 반복하면서 (어떤 거리를 가진 친구가 취약점검을 하러 갈지에 대한 순서)
        for friends in permutations(dist, len(dist)):
            count = 1  # 투입할 친구의 수
            position = weak[start] + friends[count - 1]  # 해당 친구가 점검할 수 있는 마지막 위치
            # 시작점부터 모든 취약 지점을 확인(취약 지점 개수만큼 반복하면서)

            print("투입 친구 조합", friends)

            # 취약 지점을 반복하면서(점검 시작한 위치부터 시작)
            for index in range(start, start + length):

                print("취약 지점 index", index, "/", start, start + length - 1)

                print("점검가능위치", position, "/", weak[index])

                # 점검할 수 있는 위치를 벗어나는 경우(현재 친구가 목표 취약 위치까지 도달 할 수 없는 경우)
                if position < weak[index]:
                    print("점검위치 벗어남")
                    # 새로운 친구를 투입
                    print("친구 투입")
                    count += 1
                    # 더 친구 투입이 불가능하다면 종료
                    if count > len(dist):
                        print("투입 불가")
                        print("투입한 친구", count, "투압가능한 최대친구수", len(dist))
                        break

                    # 해당 친구가 점검할 수 있는 마지막 위치
                    position = weak[index] + friends[count - 1]
                    print("다음 취약지점 위치", weak[index])
                    print("다음 친구가 가능한 거리", friends[count - 1])
                    print("친구가 점거할 수 있는 마지막위치", position)

            # 투입한 친구 최소값 계산
            answer = min(answer, count)
            print("투입한 친구 최소값", answer)
            print("조합 완료-----------------------------")
    # 투입해야되는 친구가 존재하는 친구보다 많은 경우
    if answer > len(dist):
        return -1
    return answer


print("==================================================")
print("답", solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))