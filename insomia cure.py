k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

numbers_for_k = []
numbers_for_l = []
numbers_for_m = []
numbers_for_n = []
numbers_for_d = []
a = []
flag = 0

i = 1
mul = 1

while mul <= d:
    mul = i * k
    if mul > d:
        break
    numbers_for_k.append(mul)

    if mul == 1:
        flag = d
        break
    i = i + 1

i = 1
mul = 1

while mul <= d:
    mul = i * l
    if mul > d:
        break
    numbers_for_l.append(mul)

    if mul == 1:
        flag = d
        break
    i = i + 1

i = 1
mul = 1

while mul <= d:
    mul = i * m
    if mul > d:
        break
    numbers_for_m.append(mul)

    if mul == 1:
        flag = d
        break
    i = i + 1

i = 1
mul = 1

while mul <= d:
    mul = i * n
    if mul > d:
        break
    numbers_for_n.append(mul)

    if mul == 1:
        flag = d
        break
    i = i + 1

def Union(numbers_for_k, numbers_for_l, numbers_for_m, numbers_for_n):
    final_list = list(set().union(numbers_for_k, numbers_for_l, numbers_for_m, numbers_for_n))
    return final_list

a = Union(numbers_for_k, numbers_for_l, numbers_for_m, numbers_for_n)

count = 0

for i in range(1, d + 1):
    for j in range(len(a)):
        if i == a[j]:
            count = count + 1

if flag > 0:
    print(flag)

else:
    print(count)