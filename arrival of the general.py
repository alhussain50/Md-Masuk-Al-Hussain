#144A

n = int(input())

h_list = list(map(int, input().split()))

count = 0

max_h = max(h_list)
max_index = [i for i, j in enumerate(h_list) if j == max_h]

lowest_of_max_index = max_index.index(min(max_index))
count = lowest_of_max_index - 0


min_h = min(h_list)
min_index = [i for i, j in enumerate(h_list) if j == min_h]

highest_of_min_index = min_index.index(max(min_index))
count = count + n - 1 - highest_of_min_index


if highest_of_min_index < lowest_of_max_index:
    count = count - 1


print(count)



