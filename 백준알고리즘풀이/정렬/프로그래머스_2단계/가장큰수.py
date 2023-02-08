# 1:22~ -틀림(곱하기 3하고 int형,str형 변환 하는 거 생각못함)

def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers))) # 모든 값이 0인 경우를 처리하기 위해 int변환후 str으로 변환

    return answer