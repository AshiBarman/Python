a, b = map(int, input().split())

lucky_found = False

for num in range(a, b + 1):
    s = str(num)
    if all(ch in "47" for ch in s):
        print(num, end=" ")
        lucky_found = True

if not lucky_found:
    print(-1)