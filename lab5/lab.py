import matplotlib.pyplot as plt
import numpy as np

from lab5 import filtering

def func(x):
    return np.sin(x) + 0.5


x_min = 0
x_max = np.pi
a = 0.25
k = 100

x = np.array(list(x_min + i * (x_max - x_min) / k for i in range(k)))
y = func(x)
y_noise = np.random.normal(func(x), a)
y_filtered = filtering.filter(y_noise, 0.15, 50)

line_func = plt.plot(x, y, '-', label="f(x) = sin(x) + 0.5")
line_noise = plt.plot(x, y_noise, '-', label="noise")
line_filtered = plt.plot(x, y_filtered, '-', label="filtered")

plt.setp(line_func[0], markersize=2)
plt.setp(line_noise[0], markersize=2)
plt.setp(line_filtered[0], markersize=2)
plt.grid(True)
plt.legend()
plt.show()
