#158B

n = int(input())

s = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if s[j] < s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]

count = s.count(4)
count_3 = s.count(3)

low_range_of_3 = count
i = count + count_3 - 1
j = len(s) - 1
flag = 0


while i > count - 1:
    if s[j] == 1 and s[i] == 3:
        flag = flag + 1
        count = count + 1
    j = j - 1
    i = i - 1

if count_3 > flag:
    for i in range(count_3 - flag):
        count = count + 1

count_2 = s.count(2)

temp_calc = (s.count(2) * 2) % 2

print(flag)
if temp_calc == 0:
    count = count + (count_2 / 2)

elif temp_calc != 0:
    if s.count(1) - flag >= 1: #we will not count used 1s
        k = len(s) - s.count(1)
        j = len(s) - flag - 1
        while j <= k:
            flag = flag + 1
            j = j - 1


print(flag)
print(s.count(1))
