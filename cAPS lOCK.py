s = str(input())

letters = []
count = 0

for x in s:
    letters.append(x)

if ord(letters[0]) < 123 and ord(letters[0]) > 96:
    for i in range(1, len(s)):
        if ord(letters[i]) < 91 and ord(letters[i]) > 64:
            count = count + 1
        
elif ord(letters[0]) < 91 and ord(letters[0]) > 64:
    for i in range(1, len(s)):
        if ord(letters[i]) < 91 and ord(letters[i]) > 64:
            count = count + 1

if count == len(s) - 1:
    if ord(letters[0]) < 123 and ord(letters[0]) > 96:
        for i in range(1, len(s)):
            if ord(letters[i]) < 91 and ord(letters[i]) > 64:
                letters[i] = letters[i].lower()

        letters[0] = letters[0].upper()

    elif ord(letters[0]) < 91 and ord(letters[0]) > 64:
        for i in range(1, len(s)):
            if ord(letters[i]) < 91 and ord(letters[i]) > 64:
                letters[i] = letters[i].lower()
        letters[0] = letters[0].lower()

for i in range(len(s)):
    print(letters[i], end='')