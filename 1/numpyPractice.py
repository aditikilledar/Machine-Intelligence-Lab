import numpy as np

print(np.ones(2))
print(np.ones(2, int))

print('-----------------------')

print(np.zeros(3))
print(np.zeros(3, int))

print('-----------------------')

print(np.random.rand(2,3))

print('-----------------------')

np.random.seed(0)
print(np.random.rand(1,2))
np.random.seed(0)
print(np.random.rand(1,2))

print('-----------------------')

x=[1,2,3]
print(np.array(x))

print('-----------------------')

x=[[1,2,3],[4,5,6]]
a=np.array(x)
print(a[0][0])
a[0][0] = 12
print(a)

print('-----------------------')

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.multiply(a,b))

print('-----------------------')

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.matmul(a,b))

print('-----------------------')

a=np.array([1,2])
b=np.array([3,4])
print(np.dot(a,b))

print('-----------------------')

x=np.array([[1,2],[3,4]])
print('Inverse is\n', np.linalg.inv(x))

print('-----------------------')

x=np.array([[1,2],[3,4]])
print('[[1,2],[3,4]]')
print(np.transpose(x))

print('-----------------------')

x=np.array([[1,2],[3,4]])
print(np.linalg.det(x))

print('-----------------------')

print(x.shape)