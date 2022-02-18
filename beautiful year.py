#271A

y = str(input())
y_int = int(y)

dist = 0

while dist != 1:
    count = 0
    y_int = y_int + 1
    y = str(y_int)

    digits = []

    for x in y:
        digits.append(x)

    for i in range(len(y) - 1):
        for j in range(i + 1, len(y)):
            if digits[i] == digits[j]:
                count = count + 1
    
    if count == 0:
        dist = 1
    else:
        dist = 0

print(y_int)



