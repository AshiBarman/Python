# a=int(input())
# b=int(input())
# sum=a+b
# print(sum)

# def add(a,b):
#     return a+b
# print(add(10,20))

# print(int(input())+int(input()))

# a=int(input())
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")

# a,b=map(int,input().split())
# mx=max(a,b)
# print(mx)

# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else:
#     print(b)

# a=int(input())
# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")

# N=int(input())
# sum=N*(N+1)//2
# print(sum)

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# num=int(input())
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

text=input()
vowels="aeiouAEIOU"
count=0
for i in text:
    if i in vowels:
        count+=1
print(count)