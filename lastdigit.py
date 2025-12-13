def last_digit(a, b):
    
    return pow(a, b, 10)   

def main():
    n = int(input("Enter number of test cases: "))
    for _ in range(n):
        a, b = map(int, input().split())
        print(last_digit(a, b))

main()