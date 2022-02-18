#266A

length = int(input())

stones = str(input())

list_of_stones = []

for x in stones:
    list_of_stones.append(x)

count = 0

for i in range(len(stones) - 1):
    if list_of_stones[i] == list_of_stones[i+1]:
        count = count + 1

print(count)
