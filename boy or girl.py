#236A

name = str(input())

dist_name = ''.join(set(name))

n = len(dist_name)


if n % 2 == 0:
    print("CHAT WITH HER!")

else:
    print("IGNORE HIM!")