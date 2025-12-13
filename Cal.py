exp=input()
if '+' in exp:
    A,B = exp.split('+')
    print(int(A)+int(B))
elif '-' in exp:
    A,B = exp.split('-')
    print(int(A)-int(B))
elif '*' in exp:
    A,B = exp.split('*')
    print(int(A)*int(B))
elif '/' in exp:
    A,B = exp.split('/')
    print(int(A)//int(B))