#467A

n = int(input())
matrix = []

count = 0

for i in range(n):
    r = list(map(int, input().split()))
    matrix.append(r)

for i in range(n):
    for j in range(1):
        if matrix[i][j + 1] - matrix[i][j] >= 2:
             count = count + 1


print(count)
