#11:54~

# n : 학생 수
# 국어, 영어, 수학

n = int(input())
students = []

for _ in range(n):
    students.append(input().split()) # 주의 - input.split()하면 공백으로 구분된 것들이 ","로 구분되어 리스트로 변환됨

# 복수의 기준으로 sort시 lambda 식 사용법
    # - 붙이면 내림차순
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])