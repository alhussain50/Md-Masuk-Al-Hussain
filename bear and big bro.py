#791A

a, b = [int(x) for x in input().split()]

count = 0

while a <= b:

    a = a * 3
    b = b * 2

    count = count + 1


print(count)

