#337A

n, m = [int(x) for x in input().split()]

f = list(map(int, input().split()))

f_arr = []
f_arr_diff = []
x = 0

for i in range(m - 1):
    x = abs(f[i] - f[i + 1])
    f_arr_diff.append(x)


for i in range(m - 2):
    for j in range(m - i  - 2):
        if f_arr_diff[j] > f_arr_diff[j + 1]:
            f_arr_diff[j], f_arr_diff[j + 1] = f_arr_diff[j + 1], f_arr_diff[j]

k = m - n
z = m - n
while k != 0:
    f_arr_diff.remove(f_arr_diff[m - z])
    k = k - 1
    z = z + 1


for i in range(m - 1):
    x = abs(f[i] - f[i + 1])
    for j in range(n - 1):
        if x == f_arr_diff[j]:
            f_arr.append(f[i])
            f_arr.append(f[i + 1])

print(f_arr)

