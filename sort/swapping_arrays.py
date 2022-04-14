n, k = map(int, input().split())
numA = list(map(int, input().split()))
numB = list(map(int, input().split()))

numA.sort()
numB.sort(reverse = True)

for i in range(k):
    a = numA[i]
    numA[i] = numB[i]
    numB[i] = a

print(sum(numA))
