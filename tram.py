#116A

n = int(input())

stops = []

for i in range(n):
    r = list(map(int, input().split()))
    stops.append(r)

filled_seats = []
filled_seats.append(stops[0][1])

for j in range(1, n):
    filled_seats.append(filled_seats[j - 1] + stops[j][1] - stops[j][0])

key = 0

for i in range(n - 1):
    if filled_seats[i] < filled_seats[i + 1]:
        if filled_seats[key] <  filled_seats[i + 1]:
            key = i + 1

print(filled_seats[key])
