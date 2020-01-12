from lab4 import pareto, main_criteria, saaty, convolution

mgts = (5, 5, 5, 3)
rustelecom = (6, 3, 3, 4)
akado = (1, 2, 4, 2)
qwerty = (2, 4, 4, 5)
choices = (mgts, rustelecom, akado, qwerty)
labels = ("МГТС", "Ростелеком", "Акадо", "QWERTY")
dirs = (-1, 1, 1, 1)

limits = (0.5, 0.2, 0.5)
main_criteria_choice = main_criteria.main_criteria(choices, dirs, 0, limits)
print("main criteria choice:", labels[main_criteria_choice])

pareto_choice = pareto.pareto(choices, dirs, 1, 3, labels)
print("Pareto choice:", labels[pareto_choice])

weights = (-2, 8, 4, 6)
convolution_choice = convolution.convolution(choices, weights)
print("convolution choice:", labels[convolution_choice])

saaty_choice = saaty.saaty(choices, weights)
print("Saaty choice:", labels[saaty_choice])
