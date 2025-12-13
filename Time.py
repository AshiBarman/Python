n = int(input("Enter number of works: "))

total_minutes = 0

for i in range(n):
    SH, SM, EH, EM = map(int, input().split())
    
    start = SH * 60 + SM
    end = EH * 60 + EM
    duration = end - start
    
    total_minutes += duration

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours, minutes)