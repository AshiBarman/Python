a=float(input())
b=float(input())
c=float(input())
max_num=a if (a>b and a>c) else (b if b>c else c)
print("Maximum number:",max_num)

