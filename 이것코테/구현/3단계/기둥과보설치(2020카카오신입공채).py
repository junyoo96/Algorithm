# 9:00 실패
# 9:54~11:24 실패

# 기둥
# 바닥 위에 있거나
# 보의 한쪽 끝 부분 위에 있거나
# 다른 기둥 위에 있어야함
# 보
# 한쪽 끝 부분이 기둥 위에 있거나
# 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야함
# 바닥에는 설치안됨
# 교차점 좌표 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제
# n : 벽면 크기
# build_frame : 기둥과 보를 설치하거나 삭제하는 작업 배열
# x, y: 열, 행
# a : 0 기둥, 1 보
# b: 0 삭제, 1 설치
# answer : 설치된 구조물 배열
# x,y,a
# x 좌표 기준으로 오름차순 정렬
# 같을 경우 y좌표 기준으로 오름차순 정렬
# answer : 규칙을 준수하는 올바른 구조물 배열
# x,y좌표가 모두 같은 경우 기둥이 보보다 앞으로 오면 됨
#=====================================================================================================

# 구조물 규칙에 맞는지 확인하는 함수(설치된 구조물 배열, 기둥 배열, 보 배열)
def check(answer):
    for x, y, stuff in answer:
        # 기둥이라면
        if stuff == 0:
            # 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나(해당 지점 왼쪽에 있는 경우, 해당 지점 오른쪽에 있는 경우), 또는 다른 기둥 위에 있는 경우
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:
            # 만약 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나 바닥에는 설치안되어 있다면
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True

def solution(n, build_frame):
    answer = []

    # build_frame을 반복하면서
    for x, y, stuff, operation in build_frame:
        # 만약 설치 명령이라면
        if operation == 1:
            # 구조물 배열에 해당 구조물 추가
            # 주의 - list 추가시 튜플 방식이 아닌 리스트 형태로 추가하기
            answer.append([x, y, stuff])

            # 만약 구조물 확인 함수가 false라면
            if not check(answer):
                # 구조물 삭제하기
                # 주의 - list의 remove 함수는 value 찾아서 삭제하는 것
                answer.remove([x, y, stuff])

        # elif 삭제 명령이라면
        else:
            # 구조물 배열에 해당 구조물 삭제
            answer.remove([x, y, stuff])

            # 만약 구조물 확인 함수가 true라면
            if not check(answer):
                # 구조물 다시 추가하기
                answer.append([x, y, stuff])

    # 구조물 배열 조건 맞게 정렬
    # 주의 - lambda 사용하지 않아도 기본적으로 각각의 요소에 대해 오름차순으로 졍렬
    answer.sort()
    # answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer