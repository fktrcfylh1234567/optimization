from lab4 import mko

mgts = (2, 5, 5, 3)
rustelecom = (1, 3, 3, 4)
akado = (6, 2, 4, 2)
qwerty = (5, 4, 4, 5)
choices = (mgts, rustelecom, akado, qwerty)
labels = ("МГТС", "Ростелеком", "Акадо", "QWERTY")

limits = (0.5, 0.2, 0.5)
main_criteria_choice = mko.main_criteria(choices, 0, limits)
print("main criteria choice:", labels[main_criteria_choice])

pareto_choice = mko.pareto(choices, 0, 2, labels)
print("pareto choice:", labels[pareto_choice])

weights = (2, 8, 4, 6)
