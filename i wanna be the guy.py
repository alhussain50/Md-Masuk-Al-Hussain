#469A

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

for i in range(len(p)):
    if p[i] == 0:
        p.remove(p[i])

for i in range(len(q)):
    if q[i] == 0:
        q.remove(q[i])



def Union(p, q):
    final_list = list(set().union(p, q))
    return final_list


a = Union(p, q)
if len(a) == n:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")
