import numpy as np

# a = np.array([1, 2, 3], dtype='int16')
# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

# print(b.ndim)
# print(b.shape)
# print(a.dtype)

# print(a.itemsize)
# print(b.itemsize)

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# print(a[0, :])
# print(a[:, 2])

# print(a[0, 1:6:2])

# a[1, 5] = 20
# print(a[1, :])

# a[:, 2] = 5
# print(a)

# 3d
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# to get 4
# print(b[0,1,1])

# replacing
# b[0, :, 1] = 0
# print(b)

# all zeros matrix
# zer = np.zeros((5, 7))
# print(zer)

# ones = np.ones((7,2))

# full array
# fullies = np.full((7, 8), 104)
# print(fullies)

# random numbers
# randoz = np.random.rand(4, 2)
# randoz = np.random.random_sample(a.shape)
# randoz = np.random.randint(-344, 7, size=a.shape)
# print(randoz)

# array = np.array([[1, 2, 3]])
# r1 = np.repeat(array, 3, axis=0)
# print(r1)


# output = np.ones((5, 5))
# zers = np.zeros((3, 3))
# zers[1, 1] = 9
#
# output[1:4, 1:4] = zers
#
# print(output)

# to copy
# b = a.copy()

# a = np.array([1, 2, 3, 4])
# a = a + 2
# a**power
# print(a)

# a = np.ones((2, 3))
# b = np.full((3, 2), 2)
#
# print(np.matmul(a, b))
#
# c = np.identity(3)
# d = np.linalg.det(c)
# print(d)

# stats
stats = np.array([[1, 2, 3], [4, 5, 6]])

# print(np.average(stats))
# print(np.max(stats, axis=1))
#
# before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)
#
# after = before.reshape((4, 2))
# print(after)

# stacking vectors
# v1 = np.array([1, 2, 3, 4])
# v2 = np.array([5, 6, 7, 8])
#
# print(np.vstack([v1, v2, v1, v2]))

# Horizontal  stack
# h1 = np.ones((2, 4))
# h2 = np.zeros((2, 2))
#
# print(np.hstack((h1, h2)))

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# print(filedata > 50)
# print(filedata[filedata > 50])
#
# print(np.any(filedata > 50, axis=0))
# print(np.all(filedata > 50, axis=0))
#
# print(np.any(filedata > 50, axis=1))



