n = int(input())

p = []
count = 0
sum = 0

for i in range(n):
    v = list(map(int, input().split()))
    p.append(v)
    
for i in range(n):
    sum = 0
    for j in range(3):
        sum = sum + p[i][j]
    if sum > 1:
        count = count + 1

print(count)