# emptylist=[]
# lst=['one','two','three']
# lst2=[1,2,3,4,5]
# lst3=[[1,2],[3,4],[5,6]]
# lst4=[1,2,'hii',[6,7]]
# print(emptylist)
# print(lst)
# print(lst2)
# print(lst3)
# print(lst4)

# print(len(lst2))

# lst.append('five')
# print(lst)

# lst.insert(3,'four')
# print(lst)

# lst.remove('two')
# print(lst)

# lst.append(lst2)
# print(lst)

# lst.extend(lst2)
# print(lst)

# del lst[1]
# print(lst)

# a=lst.pop(1)
# print(a)

# if 'one' in lst:
#     print(lst)
# if 'four' not in lst:
#     print("Ml")

# lst.reverse()
# print(lst)

# num=[2,4,5,8,3,2]
# sorted_lst=num.sort()
# print(num)

# num=[1,2,3,4,5,6]
# reversed_lst=num.reverse()
# print(num)

# lst=[1,9,2,7,8,5,6,4,3]
# lst2=['one','two','three']
# lst.append(lst2)
# print(lst)
# lst.extend(lst2)
# print(lst)
# a=lst.pop(2)
# print(a)
# reversed_lst=lst.reverse()
# print(lst)
# sorted_lst=lst.sort()
# print(lst)

# lst.reverse()
# print(lst)

# if 'one' in lst:
#     print(lst)
# if 'four' not in lst:
#     print("Ml")
# a=lst.pop(6)
# print(a)


# numbers=[1,5,2,9,7,45,79,25,6,18,36]
# print("Original list:",numbers)
# print("Sorted list:",sorted(numbers))
# print(numbers)

# lst=[3,1,5,4,2]
# abc=lst
# abc.append(6)
# print("list:",lst)

# NEW LECTURE DATE-7/11/25

# fruits=['apple','banana','mango','grapes','orange']
# numbers=[5,2,9,1,7]
# print("first fruit:",fruits[0])
# print("first number:",numbers[0])
# print("last fruit:",fruits[-1])
# print("last number:",numbers[-1])

# print(fruits)

# for i in range(len(fruits)):
#     print("i like:",fruits[i])

# for i in fruits:
#     print(i)

# print(len(fruits))

# fruits.append('pineapple')
# print(fruits)

# fruits.insert(2,'kiwi')
# print(fruits)

# fruits.remove('banana')
# print(fruits)

# del fruits[-1]
# print(fruits)

# fruits.pop(-1)
# print(fruits)

# if 'mango' in fruits:
#     print("yes")
# if 'mango' not in fruits:
#     print("not")

# sum=0
# for i in numbers:
#     sum+=i
#     print("sum:",sum)
# print("average:",sum/2)
# print("maximum:",max(numbers))
# print("minimum:",min(numbers))

# numbers.append(5)
# numbers.append(5)
# numbers.append(8)
# print("numbers:",numbers)
# print("total number of count:",numbers.count(5))
# print("index of 5 is:",numbers.index(5))

# lst=['x','y','z','y']
# print("index of y is:",lst.index('y'))

# fruits.reverse()
# print(fruits)

# fruits.Upper()
# print(fruits)

# A=[1,2]
# B=[3,4]
# A.extend(B)
# print(A)

# lst=[10,20,30,40,50,60,70,]
# print(lst[2])
# print(lst[2:6])

# lst=[2,3,2,4,3,5,6]
# print("original list:",lst)
# # remove repeated number


# lst=[2,3,2,4,3,5,6]
# new_lst=[]
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print("list after removing duplicates:",new_lst)

# sum of two number equal to given target

# lst=[2,3,4,5,6,7,8]
# target=15
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             print("pair is:",(lst[i],lst[j]))

# find the index of two number sum equal to given target


# lst=[2,3,4,5,6,7,8]
# target=15
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             print("index is:",(i,j))

# running sum of list

# lst=[1,2,3,4]
# running_sum=[]
# sum=0
# for i in lst:
#     sum+=i
#     running_sum.append(sum)
#     print(running_sum)

# shift multiply of zero to end of list

lst=[0,4,0,2,0,0,7,8,1,0]
non_zero=[]
zero_count=0
for i in lst:
    if i!=0:
        non_zero.append(i)
    else:
        zero_count+=1
for j in range(zero_count):
    non_zero.append(0)
print("list after shifting zeros to end:",non_zero)
print(zero_count)