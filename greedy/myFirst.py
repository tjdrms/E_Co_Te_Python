n = 25
k = 3
count = 0

while True:
    if (n % k) == 0:
        n //= k
        count += 1
        if n == 1:
            break
    else:
        n -= 1
        count += 1
        if n == 1:
            break
print(count)
