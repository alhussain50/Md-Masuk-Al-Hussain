#1030A

n = int(input())
opinions = list(map(int, input().split()))

count = 0

for i in range(n):
    if opinions[i] != 0:
        count = count + 1

if count != 0:
    print("HARD")

else:
    print("EASY")