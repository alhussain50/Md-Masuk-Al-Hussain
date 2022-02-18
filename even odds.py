#318A

n, k = [int(x) for x in input().split()]

if k <= int((n + 1) / 2):
    k = 2 * k - 1

elif k > int((n + 1) / 2):
    k = k - int((n + 1) / 2)
    k = k * 2


print(k)