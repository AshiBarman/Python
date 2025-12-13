n = int(input())
for i in range(n):
    m = int(input())
    fact=1
    for j in range(1,m+1):
        fact *= j
    print(fact)