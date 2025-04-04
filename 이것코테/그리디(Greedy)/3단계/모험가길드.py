# 9:49~
# 9:08~9:13 / 9:14~9:22(14분)

# n : 모험가 수
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여
# 최대 몇개의 모험가 그룹을 만들 수 있는지
# 최적해 방안: 공포도가 가장 낮은 모험가부터 하나씩 확인하며, 그룹에 포함될 모험가의 수를 계산할 수 있음
    # 공포도가 가장 낮은 모험가부터 오름차순으로 정렬되어 있다면, 항상 최소한의 모험가의 수만 포함하여 그룹 결성 가능
#==============================================================================================================

n = int(input())
horrors = list(map(int, input().split()))
# 공포도 리스트 오림차순 정렬 - 그룹을 만들 수 있는 최소한의 모험가 수를 보장하기 위해
horrors.sort() # 주의 - sort

answer = 0 # 모험가 그룹 수
count = 0 # 현재 모험가의 수

for horror in horrors: # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= horror: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        # 총 그룹의 수 증가시키기
        answer += 1
        # 현재 그룹에 포함된 모험가 수 초기화
        count = 0

# 총 그룹 수 출력
print(answer)