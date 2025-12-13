N = int(input())

years = N // 365
N = N % 365

months = N // 30
days = N % 30

print(years, "years")
print(months, "months")
print(days, "days")