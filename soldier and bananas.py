#546A

k, n, w = map(int, input().split())

cost = 0

for i in range(1, w + 1):
    x = k * i
    cost = cost + x


loan = cost - n

if loan < 0:
    loan = 0

print(loan)
