#158B

n = int(input())

s = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]

count = 0
i = 0
j = 0
while i < n - 1:
    while j < n:
        j = j + 1
        if s[i] + s[j] == 4:
            s.remove(s[i])
            s.remove(s[j])
            count = count + 1
            i = 0
            j = 0
        

    i = i + 1


print(count)