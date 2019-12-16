from copy import copy
import matplotlib.pyplot as plt


def main_criteria(choices, main, limits):
    maximums = list(max(choices, key=lambda a: a[i])[i] for i in range(4) if i != main)
    limits_num = list(maximums[i] * limits[i] for i in range(3))
    limits_num.insert(main, None)

    filtered = copy(choices)
    for i in (i for i in range(4) if i != main):
        filtered = list(filter(lambda it: it[i] > limits_num[i], filtered))

    opt_choice = choices.index(max(filtered, key=lambda a: a[main]))
    return opt_choice


def pareto(choices, main_x, main_y, labels):
    for i in range(4):
        plt.plot(choices[i][main_x], choices[i][main_y], 'o', label=labels[i])
    plt.grid(True)
    plt.legend()
    plt.show()

    return choices.index(max(choices, key=lambda a: a[main_x] ** 2 + a[main_y] ** 2))
