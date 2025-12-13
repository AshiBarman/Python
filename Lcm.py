def print_LCM(a,b):
    lcm=a*b
    return lcm
a=print_LCM(2,4)
print(a)

def print_GCD(a,b):
    while(b):
        temp=a%b
        a=b
        b=temp
    return a
a=print_GCD(2,4)
print(a)