import functools
import random

from prettytable import PrettyTable


def select_person(population, f, fit_sum):
    hit = random.uniform(0, 1)
    pos = 0

    for p in population:
        pos += f(p[0], p[1]) / fit_sum
        if hit < pos:
            return p


def crossover(population, f):
    descendants = list()
    fit_sum = 0

    for p in population:
        fit_sum += f(p[0], p[1])

    for i in range(2):
        a = select_person(population, f, fit_sum)
        b = select_person(population, f, fit_sum)
        descendants.append([a[0], b[1]])
        descendants.append([b[0], a[1]])

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
    pretty_table.field_names = ["N", "x", "y", "Fit", "Max fit", "Average Fit"]

    population = [[random.uniform(x1, x2), random.uniform(y1, y2)] for i in range(4)]

    for i in range(20):
        population = sorted(population, key=lambda a: f(a[0], a[1]), reverse=True)
        population += crossover(population, f)
        population = mutate(population)
        population = reduce(population, f)

        fit_sum = 0

        for p in population:
            fit_sum += f(p[0], p[1])

        max_fit_person = max(population, key=lambda a: f(a[0], a[1]))
        max_fit = f(max_fit_person[0], max_fit_person[1])
        average_fit = fit_sum / len(population)

        for person in population:
            x, y = person
            pretty_table.add_row(
                [i + 1, round(x, 4), round(y, 4), round(f(x, y), 4), round(max_fit, 4), round(average_fit, 4)])

    print(pretty_table)
    return max(population, key=lambda a: f(a[0], a[1]))
