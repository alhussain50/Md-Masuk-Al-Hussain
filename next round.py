#n = int(input("enter value of n: "))
#k = int(input("enter value of k: "))

n, k = map(int, input().split())
answer = 0

all_scores = []

#for x in range(n):
#    individual_scores = int(input())
#    all_scores.append(individual_scores)

all_scores = list(map(int, input().split()))

for i in range(k):
    if all_scores[i] > 0:
        answer = answer + 1
    else:
        break


#print(all_scores[0])

for x in range(k,n):

    if all_scores[k-1] == all_scores[x]:

        if all_scores[k-1] > 0:
            answer = answer + 1
    
    else:
        break


    

print(answer)


