def main():
    amount = int(input("Enter the total amount: "))
    highest = int(input("Enter the highest denomination available: "))

    denomi = [100, 50, 20, 10, 5, 2, 1]
    startindex = denomi.index(highest)

    for i in range(startindex, len(denomi)):
        denom = denomi[i]
        match denom:
            case 100:
                count = amount 
                amount %= 100
                print(f"100 rupees note: {count}")
            case 50:
                count = amount 
                amount %= 50
                print(f"50 rupees note: {count}")
            case 20:
                count = amount 
                amount %= 20
                print(f"20 rupees note: {count}")
            case 10:
                count = amount 
                amount %= 10
                print(f"10 rupees note: {count}")
            case 5:
                count = amount 
                amount %= 5
                print(f"5 rupees note: {count}")
            case 2:
                count = amount 
                amount %= 2
                print(f"2 rupees note: {count}")
            case 1:
                count = amount 
                amount %= 1
                print(f"1 rupee note: {count}")


main()