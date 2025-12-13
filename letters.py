X=input()
if (X.isdigit()):
    print("IS DIGIT")
elif (X.isalpha()):
    print("ALPHA")
    if(X.islower()):
        print("IS SMALL")
    else:
        print("IS CAPITAL")