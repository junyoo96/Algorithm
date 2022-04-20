n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 set 자료형에 기록
array = set(map(int, input().split()))
m = int(input())
array_request = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인 
for i in array_request:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')


