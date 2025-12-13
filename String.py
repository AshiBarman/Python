# String="ashi"
# print(String)

# String='ashi'
# print(String)

# String='''Ashi'''
# print(String)

# my_string="Hello "
# print(my_string[2])
# print(my_string[-5])
# my_string[3]="3"
# del my_string
# print(my_string)
# String=" Ashi"
# print(my_string + String)
# print(my_string*3)
count=0
for i in "Hello World":
    if i=='l':
        count += 1
print(count)
print('l' in "Hello World")
print("hello".upper())
print("hello".lower())
print("Hello I am Ashi".split())
print(''.join(["Hello ","I ","am ","Ashi "]))
print("Hello".find("o"))
s1="Bad Morning"
s2=s1.replace("Bad","Good")
print(s1)
print(s2)

# to check the string is palindrome orr not
# s="121"
# rev=""
# for i in s:
#     rev = i+rev

# if s==rev:
#     print("palin")
# else:
#     print("not")

words=s1.split()
words.sort()
for i in words:
    print(i)