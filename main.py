import numpy as np

x = np.array([1,2,3,4])
X = np.array([[1,2],[3,4],[5,6],[7,8]])
dot = x.dot(X)
XT = X.transpose()

print('Vector: \n', x)
print('\nMatrix: \n', X)
print('\nMultiplication: \n', dot)
print('\nTranspose: \n', XT)