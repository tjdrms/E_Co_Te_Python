n, k = map(int, input().split())
numA = list(map(int, input().split()))
numB = list(map(int, input().split()))

numA.sort()
numB.sort(reverse = True)

for i in range(k):
    if numA[i] < numB[i]:
        numA[i], numB[i] = numB[i], numA[i] 
    else:
        break

print(sum(numA))
