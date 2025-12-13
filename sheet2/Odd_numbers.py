t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x > y:
        x,y = y,x
    s=0
    for j in range(x + 1,y):
        if j % 2 == 1:
            s += j
    print(s)