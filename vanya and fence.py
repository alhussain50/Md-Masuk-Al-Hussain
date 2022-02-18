#677A

n, h = input().split()

h = int(h)
n = int(n)

a = list(map(int, input().split()))

count = 0

for i in range(len(a)):
    if a[i] > h:
        count = count + 2

    else:
        count = count + 1


print(count)