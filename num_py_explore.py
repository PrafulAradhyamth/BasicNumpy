import numpy as np
#Basics
a=np.array([1,2,3])
print(a)
#float 64
b=np.array([[1.25,2.35,3.78],[4,5,6],[7,8,9]])
print(b)

b.ndim

c=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

c.ndim

c.shape

c.size

c.dtype

a=np.array([1,2,3],dtype='int16')

print('"a" take up '+ str(a.itemsize) +' bytes of memory')
print('number of elements in the array are '+ str(a.size))
print('the total size occupied by this array is '+str(a.size*a.itemsize)+'bytes')

print(str(a.nbytes)+'bytes')

a=np.array([[45689,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(a[0,0])

print(a[0,:])

#[start:end:stepsize]
print(a[0,2:9:3])
#replace
a[0,:]=5
print(a)

#outside in for 3D indexing

a=np.zeros((3,3))
print(a)


print(np.ones((3,3)))
#(shape,what number u want to fill)
a=np.full((2,2),112)
print(a)
#fulllike

c=np.full_like(a,112)
#random
np.random.rand(4,3,2)

np.random.random_sample(a.shape)


#random inte
np.random.randint(5,77,size=(4,3))

#indentity
np.identity(3)
#repeat
#[] and [[]]
#axis 0 and axis1
a=np.array([[1,2,3]])
r1=np.repeat(a,3,axis=1)
print(r1)

#coping
a=np.array([1,2,3])
b=a.copy()
c=a
c[0]=112
print(b)
print(c)
print(a)
#becarefull

# mathematics
a=np.array([1,2,3])
b=np.array([5,8,9])
print(a+2)
print(a+b)
print(a*b)
print(a/b)
print(a**b)
print(np.cos(a))

#linear algebra
#for matrix multiplication
a=np.array([1,2,3])
b=np.array([5,8,9])
np.matmul(a,b)

