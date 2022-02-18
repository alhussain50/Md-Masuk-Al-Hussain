#266B

n, t = [int(x) for x in input().split()]

s = str(input())

char_list = []

for a in s:
    char_list.append(a)

i = 0
j = 0

while i < t:
    while j < n - 1:
        if char_list[j] == 'B' and char_list[j + 1] == 'G':
            char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
            j = j + 2

        else:
            j = j + 1

    i = i + 1
    j = 0

for i in range(n):
    print(char_list[i], end='')


