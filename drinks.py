#200B

n = int(input())
p = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum = sum + p[i]


sum = sum / n
print(sum)