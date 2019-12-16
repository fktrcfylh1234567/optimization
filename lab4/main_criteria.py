from copy import copy


def choice(choices, main, limits):
    maximums = list(max(choices, key=lambda a: a[i])[i] for i in range(4) if i != main)
    limits_num = list(maximums[i] * limits[i] for i in range(3))
    limits_num.insert(main, None)

    filtered = copy(choices)
    for i in (i for i in range(4) if i != main):
        filtered = list(filter(lambda it: it[i] > limits_num[i], filtered))

    opt_choice = choices.index(max(filtered, key=lambda a: a[main]))
    return opt_choice
