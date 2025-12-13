def print_even(n):
    if n<0:
        return
    print_even(n-1)
    if n%2==0:
        print(n,end='')
print_even(11)