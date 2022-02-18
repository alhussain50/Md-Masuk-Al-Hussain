#59A

s = str(input())

letters = []

for x in s:
    letters.append(x)

count_cap = 0
count_small = 0

for i in range(len(s)):
    if ord(letters[i]) < 91 and ord(letters[i]) > 64:
        count_cap = count_cap + 1

    elif ord(letters[i]) < 123 and ord(letters[i]) > 96:
        count_small = count_small + 1


if count_cap > count_small:
    print(s.upper())

else:
    print(s.lower())
