import numpy as np
# a=np.array([0,1,2,3,4])
# print(a.ndim)
# print(a.shape)
# print(len(a))
# print(s)
# print(np.arange(10))


# {run in jupiter notebook}
# L = range(1000)
# print(%timeit  (a**2 for i in L))


# a=np.array([[0,1,2,],[6,7,8]])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(len(a))

# a=np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
# print(a.ndim)
# print(a.shape)

# a=np.array([0,1,2,3,4])
# print(np.arange(10))

a=np.linspace(0,1,6)
print(a)

# a=np.zeros((3,5))
# print(a)
# a=np.ones((3,5))
# print(a)

# a=np.eye(3)
# print(a)

# a=np.diag([1,2,3,4])
# print(a)
# np.diag(a)

# a=np.random.rand(4)
# print(a)

# normal distribution

# a=np.arange(10.0)
# print(a.dtype)

# a=np.random.randn(4)
# print(a)

# a=np.zeros((3,5))
# print(a.dtype)

# a=np.array([(1+2),(3+4)])
# print(a.dtype)

# a=np.array([True,False])
# print(a.dtype)

# a=np.array(['hii','hello','byee'])  U6 is unique code,means it is a string and 6 is size means it has 6 value numpy
# print(a.dtype)

# a=np.arange(10)
# print(a[5])

# a=np.diag([1,2,3])
# print(a[2,2])
# a[2,2]=5
# print(a)

# a=np.arange(1,10,2)
# print(a)

# a=np.arange(10)
# a[5:]=0
# print(a)

# b=np.arange(5)
# a[5:]=b[::-1]
# print(a)

# a=np.arange(10)
# print(a)
# b=a[::2]
# print(b)
# print(np.shares_memory(a,b))
# print(np.shares_memory(b,a))

# c=a[::2].copy()
# print(c)
# print(np.shares_memory(a,c))

# a=np.random.randint(0,20,15)
# print(a)

# mask = (a%2==0)
# print(mask)

# extract_from_a = a[mask]
# print(extract_from_a)

# a[mask] = -1
# print(a)

# a=np.arange(0,100,10)
# print(a)

# a[[2,3,4]] = 1
# print(a)

# a[[9,7]] = -200
# print(a)


# <--------------Operations--------------->

import numpy as np

# a = np.array([1,2,3,4])
# print(a + 1)

# a = np.array([1,2,3,4])
# print(a ** 2)

# b=np.ones(4) + 1
# print(a-b)
# print(a*b)
# print(a+b)

# c=np.diag([1,2,3,4])
# print(c*c)
# print("*****")
# print(c.dot(c))

# a=np.array([1,2,3,4])
# d=np.array([1,4,5,6])
# print(a==d)
# print(a>b)

# a=np.array([1,2,3,4])
# b=np.array([1,4,5,6])
# c=np.array([1,2,3,4])
# print(np.equal(a,b))
# print(np.equal(a,c))
# print(np.logical_and(a,b))

# a=np.arange(5)
# print(np.sin(a))
# print(np.cos(a))
# print(np.log(a))
# print(np.tan(a))
# print(np.exp(a))

# a=np.arange(4)
# print(a+np.array(([2,3])))

# a=np.array([1,2,3,4])
# print(np.sum(a))

# a=np.array([[1,1],[2,2]])
# print(a)
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.min())
# print(a.max())
# print(a.argmin())
# print(a.argmax())
# print(np.all([True,True,False]))
# print(np.any([True,True,False]))

# a=np.zeros([50,50])
# print(np.any(a != 0))
# print(np.all(a == 0))

# a=np.array([1,2,3,2])
# b=np.array([2,2,3,2])
# c=np.array([6,4,4,5])
# print(((a <= b) & (b <= c)).all())

# a=np.array([1,2,3,1])
# b=np.array(([1,2,3],[5,6,1]))
# print(a.mean())
# print(np.median(a))
# print(np.median(b,axis=-1))
# print(a.std())

# import numpy as np

a = np.tile(np.arange(0,40,10),(3,1))
print(a)

print("*************")
a = a.T
print(a)

b = np.array([0,1,2])
print(b)
print("**************")
print(a)
print("***************")
print(a)
print("###############")
p