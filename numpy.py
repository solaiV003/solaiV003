import numpy as np
#1 1D array
a = np.array((1, 2, 3, 4, 5))
print("#1",a)
#2 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("#2",a)
a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("#3",a)
#check number of dimentions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("dimentions are:")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#indexing for 1D
arr = np.array([1, 2, 3, 4])
print(arr[1])
#for 2D
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', a[0, 1])
#for 3D
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[0, 1, 2])
#slicing
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a[4:])
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a[1:5:2])
#iterations
a = np.array([1, 2, 3])
for x in a:
  print(x)
