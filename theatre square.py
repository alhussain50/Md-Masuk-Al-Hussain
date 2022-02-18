#1A

n, m, a = [int(i) for i in input().split()]

x = n / a
x = int(x)

y = m / a
y = int(y)

x_rem = n % a
y_rem = m % a

if x_rem != 0:
    x = x + 1

if y_rem != 0:
    y = y + 1

result = x * y
print(result)
    