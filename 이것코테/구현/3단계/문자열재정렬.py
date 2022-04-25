a = list(input())

alphabet = []
num = []

for i in a:
    if i.isalpha():
        alphabet.append(i)
    else:
        num.append(i)

alphabet.sort()
num_sum = sum(list(map(int,num)))

print(str(alphabet) + str(num_sum))