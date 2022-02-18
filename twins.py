#160A

n = int(input())

value_of_coins = list(map(int, input().split()))

count = 1

for i in range(n - 1):
    for j in range(n - i - 1):
        if value_of_coins[j] <  value_of_coins[j + 1]:
            value_of_coins[j], value_of_coins[j + 1] = value_of_coins[j + 1], value_of_coins[j]

total_sum = value_of_coins[0]

for i in range(n - 1):
    total_sum = total_sum + value_of_coins[i + 1]


total_sum = total_sum / 2
total_sum = int(total_sum)

sum_of_stolen_coins = value_of_coins[0]

for i in range(n - 1):
    
    if sum_of_stolen_coins > total_sum:
        break

    else:
        sum_of_stolen_coins = sum_of_stolen_coins + value_of_coins[i + 1]
        count = count + 1


print(count)