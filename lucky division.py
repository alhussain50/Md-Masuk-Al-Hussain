#122A

n = int(input())

str_n = str(n)

lenght_of_n = len(str_n)

digits = []

count = 0

for x in str_n:
    digits.append(x)

for i in range(lenght_of_n):
    if digits[i] == '4':
        count = count + 1

    elif digits[i] == '7':
        count = count + 1

if count == lenght_of_n:
    print("YES")

else:
    if n % 4 == 0 or n % 7 == 0 or n % 47 == 0 or n % 74 == 0:
        print("YES")

    else:
        print("NO")

    