import random

from prettytable import PrettyTable


def crossover(population):
    descendants = [
        [population[0][0], population[1][1]],
        [population[0][0], population[2][1]],
        [population[1][0], population[0][1]],
        [population[2][0], population[0][1]]
    ]
    return descendants


def mutate(population):
    for person in population:
        if random.uniform(0, 1) < 0.25:
            person[0] = random.uniform(person[0] - 0.1, person[0] + 0.1)
            person[1] = random.uniform(person[1] - 0.1, person[1] + 0.1)
    return population


def reduce(population, f):
    for i in range(4):
        population.remove(min(population, key=lambda a: f(a[0], a[1])))
    return population


def search(f, x1, x2, y1, y2):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["N", "x", "y", "Fit"]

    population = [[random.uniform(x1, x2), random.uniform(y1, y2)] for i in range(4)]

    for i in range(10):
        population = sorted(population, key=lambda a: f(a[0], a[1]), reverse=True)
        population += crossover(population)
        population = mutate(population)
        population = reduce(population, f)

        for person in population:
            x, y = person
            pretty_table.add_row([i + 1, round(x, 4), round(y, 4), round(f(x, y), 4)])

    print(pretty_table)
