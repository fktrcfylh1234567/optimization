import matplotlib.pyplot as plt


def plot(x, orig, noise, filtered):
    line_func = plt.plot(x, orig, '-', label="f(x) = sin(x) + 0.5")
    line_noise = plt.plot(x, noise, '-', label="noise")
    line_filtered = plt.plot(x, filtered, '-', label="filtered")

    plt.setp(line_func[0], markersize=2)
    plt.setp(line_noise[0], markersize=2)
    plt.setp(line_filtered[0], markersize=2)
    plt.grid(True)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
