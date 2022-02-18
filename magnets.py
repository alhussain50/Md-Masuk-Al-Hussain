#344A

n = int(input())
magnets = []


for i in range(n):
    temp = input()
    magnets.append(temp)

count = 0

for i in range(n - 1):
    if magnets[i] != magnets[i + 1]:
        count = count + 1


count = count + 1 
print(count)