import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

fig = plt.figure(figsize=(10, 5))
pretty_table = PrettyTable()
pretty_table.field_names = ["N", "x", "y", "Fit", "Max fit", "Average Fit"]


def select_person(population, f):
    fit_sum = 0
    for p in population:
        fit_sum += f(p[0], p[1])

    hit = random.uniform(0, 1)
    pos = 0

    for p in population:
        pos += f(p[0], p[1]) / fit_sum
        if hit < pos:
            return p


def crossover(population, f):
    descendants = list()

    for i in range(2):
        a = select_person(population, f)

        a_index = population.index(a)
        candidates = [population[i] for i in range(4) if i != a_index]
        b = select_person(candidates, f)

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
    population = [[random.uniform(x1, x2), random.uniform(y1, y2)] for i in range(4)]

    for i in range(100):
        population = sorted(population, key=lambda a: f(a[0], a[1]), reverse=True)
        population += crossover(population, f)
        population = mutate(population)
        population = reduce(population, f)

        if (i + 1) % 10 == 0:
            show_population(population, f, i + 1)

    print(pretty_table)
    plt.show()

    return max(population, key=lambda a: f(a[0], a[1]))


def show_population(population, f, i):
    fit_sum = 0
    for p in population:
        fit_sum += f(p[0], p[1])

    max_fit_person = max(population, key=lambda a: f(a[0], a[1]))
    max_fit = f(max_fit_person[0], max_fit_person[1])
    average_fit = fit_sum / len(population)

    for p in population:
        x, y = p
        pretty_table.add_row(
            [i, round(x, 4), round(y, 4), round(f(x, y), 4), round(max_fit, 4), round(average_fit, 4)]
        )

        fft_axes = fig.add_subplot(2, 5, i / 10)
        fft_axes.set_title(str(round(i)))
        fft_axes.set_autoscaley_on(False)
        fft_axes.set_ylim([-1, 1])
        fft_axes.set_xlim([-1, 1])
        fft_axes.plot(p[0], p[1], 'x')
