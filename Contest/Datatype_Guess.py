n,k,a=map(int,input().split())
num = n * k
if num % a != 0:
    print("double")
else:
    value = num // a
    int_min = -2147483648
    int_max = 2147483647
    LL_min = -9223372036854775808
    LL_max = 9223372036854775807
    if int_min <= value <= int_max:
        print("int")
    elif LL_min <= value <= LL_max:
        print("long long")
    else:
        print("double")

