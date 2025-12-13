def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fabo(n-1)+fabo(n-2)
for i in range (10):
    print(fabo(i))