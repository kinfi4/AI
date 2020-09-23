import numpy as np

#найти подходящие веса
weights = np.array([[0., 0., 0.]])
examples = np.array([
    [1, 1, 0.3],
    [1, 0.4, 0.5],
    [1, 0.7, 0.8]
])


def Predict(ex):
    sum = weights.dot(ex)

    return 1 if sum > 0 else 0

def Target(ex):
    if ex[1] == 1 and ex[2] == 0.3:
        return 1
    if ex[1] == 0.4 and ex[2] == 0.5:
        return 1
    if ex[1] == 0.7 and ex[2] == 0.8:
        return 0


perfect = False
while not perfect:
    perfect = True
    for ex in examples:
        if Target(ex) != Predict(ex):
            perfect = False
            if Predict(ex) == 1:
                weights -= ex
            elif Predict(ex) == 0:
                weights += ex

#1 1.6 -3.1

print(weights)

























