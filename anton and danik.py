n = int(input())
s = str(input())

letters = []

for x in s: 
    letters.append(x)

count_A = 0
count_D = 0

for i in range(len(s)):
    if letters[i] == 'A':
        count_A = count_A + 1

    if letters[i] == 'D':
        count_D = count_D + 1


if count_A > count_D:
    print("Anton")

elif count_A < count_D:
    print("Danik")

elif count_D == count_A:
    print("Friendship")