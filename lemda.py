# a=2
# b=4
# int=lambda a,b:a+b
# print(int(a,b))


# int=lambda x:(x%10)+(x//10)
# print(int(32))


# sum=lambda x:sum(x//10)+x%10 if x>0 else 0
# print(sum(12334))

sum=lambda x:sum(x//10)+x%10 if x>0 else 0
print(sum(1234567890))