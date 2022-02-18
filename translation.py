#41A

s = str(input())
t = str(input())
count = 0

letters_of_s = []
letters_of_t = []

for x in s:
    letters_of_s.append(x)

for x in t:
    letters_of_t.append(x)

high_range = len(s) / 2
high_range = int(high_range)


i = 0
j = len(s) - 1

while i < high_range:
    while j >= high_range:
        letters_of_s[i], letters_of_s[j] = letters_of_s[j], letters_of_s[i]
        j = j - 1
        break
    i = i + 1

for i in range(len(t)):
    if letters_of_s == letters_of_t:
        count = count + 1

if count == len(s):
    print("YES")

else:
    print("NO")
