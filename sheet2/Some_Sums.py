N,A,B = map(int,input().split())
total = 0
for i in range(1,N+1):
    s = 0
    temp = i
    while temp > 0 :
        s += temp % 10
        temp //= 10
    if A <= s <=B :
        total += i
print(total)