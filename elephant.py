#617A

n = int(input())

count = 0

while n % 5 != 0:
    if n % 5 == 1:
        n = n - 1

    elif n % 5 == 2:
        n = n - 2

    elif n % 5 == 3:
        n = n - 3

    elif n % 5 == 4:
        n = n - 4

    count = count + 1

while n % 5 == 0:

    if n == 0:
        break

    
    n = n - 5
    count = count + 1

    

print(count)