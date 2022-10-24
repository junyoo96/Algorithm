#2020 카카오 블라인드 코딩테스트
# ?
# 12:56~ / 구현못함

# answer : 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이
def solution(s):
    length = len(s)
    answer = length

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, length // 2 + 1):
        # 압축한 문자열 변수
        compressed = ""
        # 현재 문자열
        # 주의 - 앞뒤의 요소를 비교할 경우 앞요소 이후의 뒤요소부터 반복수행하는 방식으로 구현하기
        prev = s[:step]
        # 문자열 압축 반복 횟수 변수
        cnt = 1
        # 주의 - 문자열 단위만큼 증가시키며 현재 문자열과 비교
        for i in range(step, length, step):
            # 만약 현재 문자열과 비교 문자열이 같다면
            if prev == s[i: i + step]:
                # 문자열 압축 반복 횟수 증가
                cnt += 1
            else:
                # 압축을 한번이라도 했었다면
                if cnt >= 2:
                    compressed += str(cnt) + prev
                # 압축한적 없다면
                else:
                    compressed += prev

                # 현재 문자열 초기화
                prev = s[i: i + step]
                # 압축 반복 횟수 초기화
                cnt = 1

        #문자열 단위보다 비교할 문자열 길이가 적게 남아있는 경우, 남아 있는 문자열에 대해서 처리(for문 에서 이미 마지막 문자열까지 압축가능한지 확인했기 때문에 압축된 문자열만 처리해주면 됨
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        # 단위(step)마다, 만들어지는 압축 문자열이 가장 짧은 것을 갱신
        answer = min(answer, len(compressed))

    return answer