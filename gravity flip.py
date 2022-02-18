n = int(input())

columns = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if columns[j] > columns[j + 1]:
            columns[j], columns[j + 1] = columns[j + 1], columns[j]


for i in range(n):
    print(columns[i], end=' ')

