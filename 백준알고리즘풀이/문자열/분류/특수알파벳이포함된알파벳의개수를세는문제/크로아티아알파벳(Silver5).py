# 11:08~

# answer : 몇개의 크로아티아 알파벳으로 이루어져 있는지 출력

c_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in range(len(c_alphabets)):
    word = word.replace(c_alphabets[i], str(i)) # 주의 - replace함수는 원본 문자열을 변경하지 않음

print(len(word))