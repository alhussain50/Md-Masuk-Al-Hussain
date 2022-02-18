#479A

a = int(input())
b = int(input())
c = int(input())

results = []
temp = 0

temp = a + b + c
results.append(temp)

temp = a + b * c
results.append(temp)

temp = a * (b + c)
results.append(temp)

temp = a * b * c
results.append(temp)

temp = (a + b) * c
results.append(temp)

maxResult = max(results)
print(maxResult)

