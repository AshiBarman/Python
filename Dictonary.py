# my_dict = {}
# my_dict = {1:'abc',2:'hello'}
# my_dict = {'name':'ashi',1:'abc',2:'hello'}
# print(my_dict)

# my_dict = dict()
# my_dict = dict([(1,'abc'),(2,'ijk')])
# print(my_dict)

# my_dict={}
# my_dict={'name':'abc','age':'12','address':'panagar'}
# print(my_dict['name'])

# key error
# my_dict={}
# my_dict={'name':'abc','age':'12','address':'panagar'}
# print(my_dict.get('kjb'))
# change the value of any key
# my_dict['age']='13'
# print(my_dict)

# to add a new key
# my_dict['degree']='b-tech'
# print(my_dict)

# to delete any key
# print(my_dict.pop('age'))
# print(my_dict)

# to delete item from last
# my_dict.popitem()
# print(my_dict)

# square={1:23,2:67,3:89}
# del square[2]
# square.clear()
# del square
# print(square)
# my_dict=square.copy()
# print(my_dict)

# my_dict={}.fromkeys(['ashii','sjfif','hiff'],0)
# print(my_dict)

# subjects={2:4,3:9,4:16}
# print(subjects.items())
# print(subjects.keys())
# print(subjects.values())

# d={}
# print(dir(d))

# compreshension
d={1:1,2:4,3:9,4:16}
# for pair in d.items():
#     print(pair)

# my_dict={k:v for k,v in d.items() if v>1}
# print(my_dict)

d={k + 2 : v*2 for k,v in d.items() if v>2}
print(d)