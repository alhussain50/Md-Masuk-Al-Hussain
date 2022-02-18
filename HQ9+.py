#133A

p = str(input())

letters = []

for x in p:
    letters.append(x)

count = 0

for i in range(len(p)):
    if letters[i] == 'H' or letters[i] == 'Q' or letters[i] == '9':
        count = count + 1

if count != 0:
    print("YES")

else:
    print("NO")