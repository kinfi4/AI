from urllib import request
import numpy as np
fname = "https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"
file = request.urlopen(fname)
data = np.loadtxt(file, delimiter=',', skiprows=1)

# print(data)
Y = data[:, 0]
X = data[:, 1:]

newcol = np.array([[1 for i in range(X.shape[0])]]).reshape((X.shape[0]), 1)
X = np.column_stack((newcol, X))

PredictVector = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

print(Y)
print()
print()
print(list(map(int, Y - X.dot(PredictVector))))