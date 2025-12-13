n=input("Enter a number:")
s= lambda x:all(x[i] == x[-i-1] for i in range(len(x)//2))
if s(n):
    print(f"{n} is  a palindrome")
else:
    print(f"{n} is not a palindrome")