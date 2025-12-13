t=int(input())
for i in range(t):
    n=int(input())
    ones=bin(n).count("1")
    binary_num="1"*ones
    result=int(binary_num,2)
    print(result)