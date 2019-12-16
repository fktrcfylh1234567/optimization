from lab4 import main_criteria

mgts = (2, 5, 5, 3)
rustelecom = (1, 3, 3, 4)
akado = (6, 2, 4, 2)
qwerty = (5, 4, 4, 5)
choices = (mgts, rustelecom, akado, qwerty)

limits = (0.5, 0.2, 0.5)
main_criteria_choice = main_criteria.choice(choices, 0, limits)
print("main criteria choice:", main_criteria_choice + 1)

weights = (2, 8, 4, 6)
