import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)


a = np.exp(-(abs(x)/10))
b = 1 + np.tan(1/(1 + np.sin(x)**2))
c = x**2 + 1
y = np.log(a*c) / np.log(b)

plt.plot(x, y)
plt.show()

