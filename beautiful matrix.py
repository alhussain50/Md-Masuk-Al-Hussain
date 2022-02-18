#263A

matrix = []

for i in range(5):
    value = list(map(int, input().split()))
    matrix.append(value)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            i = 2 - i
            i = abs(i)
            j = 2 - j
            j = abs(j)
            answer = i + j
            
print(answer)