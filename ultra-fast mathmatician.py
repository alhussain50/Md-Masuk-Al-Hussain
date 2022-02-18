a = str(input())
b = str(input())

m = []
n = []
o = []

for x in a:
    m.append(x)

for y in b:
    n.append(y)


for i in range(len(n)):
    if m[i] == n[i]:
        o.append('0')

    else:
        o.append('1')

for i in range(len(n)):
    print(o[i], end='')