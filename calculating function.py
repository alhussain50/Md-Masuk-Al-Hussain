#486A

n = int(input())

if n % 2 != 0:
    result = int((n + 1) / 2)
    result = -(result)

else:
    result = int(n / 2)

print(result)