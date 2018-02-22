import math

import numpy as np
from matplotlib import pyplot

pi = math.pi
x = np.linspace(0, 2 * pi, 1000)
y = np.sin(x) * np.cos(x)

pyplot.plot(x, y, label="sin*cos")
y = np.sin(x)
pyplot.plot(x, y, label="sin")
y = np.cos(x)
pyplot.plot(x, y, label="cos")

pyplot.title("Sin * Cos Graph")

pyplot.xlabel("X-Axis")
pyplot.ylabel("Y-Axis")

pyplot.legend()

pyplot.show()
