import numpy as np

a=np.array([0,1,2])
print type(a)

print a.shape

print a[0]

# 2 d array
b=np.array([[0,1,2],[3,4,5]])
print type(b)
print b
print b.shape

#create a 3*3 with all zero
a=np.zeros((3,3))
print a
#create a 3*3 with one
a=np.ones((2,2))
print a
#create a 3*3 coonstant array
a=np.full((3,3),7)
print a
#random array
a=np.random.random((3,3))
print a
#identity matrix
a=np.eye(3)
print a, type(a)
#convert list to array
a=np.array([2,3,4,5,1])
print a, type(a)
#arange() will create array with regurally increment values 
a=np.arange(20)
print a
a=np.array([[0,1.2,0],[0,0,0],[1+1j,3,2.]])
print a
a=np.linspace(2.,4.,10)
print a