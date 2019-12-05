import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def make_plot(fun, x1, x2, y1, y2, x_max, y_max, z_max):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(x1, x2, 0.05)
    y = np.arange(y1, y2, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array(fun(np.ravel(X), np.ravel(Y)))
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    point = ax.plot([x_max], [y_max], [z_max], 'o')
    plt.setp(point[0], markersize=10)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
