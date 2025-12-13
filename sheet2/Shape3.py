#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *


n=int(input())
#upperhalf
for i in range(1,n+1):
    star="*"*(2*i-1)
    line=star.rjust(n+i-1)
    print(line)
#lowerhalf
for i in range(n,0,-1):
    star="*"*(2*i-1)
    line=star.rjust(n+i-1)
    print(line)
