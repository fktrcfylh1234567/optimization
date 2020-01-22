from functools import reduce

import numpy as np
from prettytable import PrettyTable


def saaty(choices, weights, labels):
    consistency(choices, labels)

    choices = [[sum(choices[i][cr] / choices[j][cr] for j in range(4)) for i in range(4)] for cr in range(4)]
    choices = np.array(choices).transpose()
    choices = choices / np.abs(choices).sum(axis=0)

    weights = [sum(weights[i] / weights[j] for j in range(4)) for i in range(4)]
    weights = np.array(weights).transpose()
    weights = weights / np.abs(weights).sum(axis=0)

    res = np.dot(choices, weights)
    return np.where(res == np.amax(res))[0][0]


def consistency(choices, labels):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["Choice", labels[0], labels[1], labels[2], labels[3]]

    for crit in range(4):
        matrix = [[choices[i][crit] / choices[j][crit] for j in range(4)] for i in range(4)]

        for i in range(4):
            row = [labels[i]]
            row += matrix[i]
            pretty_table.add_row(row)

        print(pretty_table)

        matrix = np.array(matrix)

        # Own vectors
        vecs = [reduce(lambda a, b: a * b, matrix[i]) ** (1 / 4) for i in range(4)]

        # Sums
        matrix = matrix.transpose()
        s = np.array([sum(matrix[i]) for i in range(4)])

        # Normalizing own vectors
        vecs_norm = [vecs[i] / s[i] for i in range(4)]

        # Own value
        own_val = sum(s * vecs_norm)

        consistency_index = (own_val - 4) / 3
        consistency_ratio = consistency_index / 0.9

        print("consistency ratio:", consistency_ratio)
        pretty_table.clear_rows()
        print()
