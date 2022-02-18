#977A

n, k = [int(x) for x in input().split()]



for i in range(k):
    str_n = str(n)
    if str_n[-1] == '0':
        n = n / 10
        n = int(n)

    else:
        n = n - 1

print(n)