#96A

x = str(input())

players = []

for i in x:
    players.append(i)

count = 0
n = 0


for j in range(len(x) - 1):
    if players[j] == players[j + 1]:
        count = count + 1
        if count >= 6:
            n = count
    elif players[j] != players[j + 1]:
        count = 0



if n > 5:
    print("YES")

else:
    print("NO")