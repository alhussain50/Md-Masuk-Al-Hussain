n = int(input())

count = 0

for m in range(n):

    statement = str(input())
    statement = statement.translate({ord(i): None for i in 'xX'})

    if statement == '++':
        count = count + 1
    elif statement == '--':
        count = count - 1

print(count)