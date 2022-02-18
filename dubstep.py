#208A

s = str(input())
letters = []


s = s.replace("WUB", " ")

for x in s:
    letters.append(x)


print(s)

n = len(s)
i = 0

while i < n - 1:
    if letters[i] == ' ' and letters[i + 1] == ' ':
        letters.remove(letters[i])
        n = n - 1

    i = i + 1

if letters[0] == ' ':
    letters.remove(letters[0])

for i in range(len(letters)):
    print(letters[i], end='')