def reverse(n):
    return int(str(n)[::-1])

c=int(input())

for _ in range(c):
    a,b=map(int,input().split())
    rev_a=reverse(a)
    rev_b=reverse(b)
    s=rev_a+rev_b
    print(reverse(s))