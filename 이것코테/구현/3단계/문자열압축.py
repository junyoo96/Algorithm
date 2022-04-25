#2020 카카오 블라인드 코딩테스트
def solution(s):
    length = len(s)
    answer = length

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, length // 2 + 1):
        compressed = "" # 압축된 문자열 저장
        prev = s[:step] # 앞에서 step 만큼 문자열 추출
        cnt = 1 # 문자열 압축 가능 여부 판별
        # 단위(step) 만큼 증가시키며 이전 문자열과 비교
        for j in range(step, length, step):
            #현재 문자열 prev와 뒤 문자열 같은지 비교
            if prev == s[j: j + step]:
                # 압축 반복된 횟수 증가
                cnt += 1
            else:
                # 압축이 한번이라도 반복 되었다면
                if cnt >= 2:
                    compressed += str(cnt) + prev
                # 압축할게 없었다면
                else:
                    compressed += prev
                # 다시 현재 문자열 초기화
                prev = s[j: j + step]
                # 압축 반복 횟수 초기화
                cnt = 1

        #남아 있는 문자열에 대해서 처리(for문 에서 이미 마지막 문자열까지 압축가능한지 확인했기 때문에 압축된 문자열만 처리해주면 됨
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        # 단위(step)마다, 만들어지는 압축 문자열이 가장 짧은 것을 확인
        answer = min(answer, len(compressed))
    return answer
