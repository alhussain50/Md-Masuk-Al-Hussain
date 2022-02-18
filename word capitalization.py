#281A

word = str(input())

letters = []

for i in word:
    letters.append(i)

letters[0] = letters[0].upper()

for x in range(len(letters)):
    print(letters[x], end='')