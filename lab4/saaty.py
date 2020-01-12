import numpy as np


def saaty(choices, weights):
    choices = [[sum(choices[i][cr] / choices[j][cr] for j in range(4)) for i in range(4)] for cr in range(4)]
    choices = np.array(choices).transpose()
    choices = choices / np.abs(choices).sum(axis=0)

    weights = [sum(weights[i] / weights[j] for j in range(4)) for i in range(4)]
    weights = np.array(weights).transpose()
    weights = weights / np.abs(weights).sum(axis=0)

    res = np.dot(choices, weights)
    return np.where(res == np.amax(res))[0][0]
