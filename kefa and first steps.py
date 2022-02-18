#580A

n = int(input())
a = list(map(int, input().split()))


if n == 1:
    print("1")

else:
    list_of_count = []

    count = 1

    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            count = count + 1

        else:
            count = 1

        list_of_count.append(count)


    output = max(list_of_count)
    print(output)