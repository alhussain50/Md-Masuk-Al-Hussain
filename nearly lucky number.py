#110A

n = int(input())
str_n = str(n)

digits = []
count = 0

for x in str_n:
    digits.append(x)

number_of_digits = len(digits)

for i in range(number_of_digits):
    if digits[i] == '4' or digits[i] == '7':
        count = count + 1

if count == 4 or count == 7:
    print("YES")

else:
    print("NO")