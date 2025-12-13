# a=input("Enter first number:")
# b=input("Enter second number:")
# print("Select operation")
# print("1.Addition,2.Subtraction,3.Multiplication,4.Division")
# choice=input("Enter choice(1/2/3/4):")
# match choice:
#     case '1':print(a+b)
#     case '2':print(a-b)
#     case '3':print(a*b)
#     case '4':print(a/b)


def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    if b==0:
        return "Error"
    else:
        return a/b
        
    