import numpy as np
import matplotlib.pyplot as plt

x = np.arange(11)

y=x

plt.plot(x, y, color ='orange', label = 'x+2')
plt.plot(x,y, color = 'blue', label = 'x+3')

plt.xlabel("x")
plt.ylabel("y")
plt.title("line chart with two lines")

plt.legend()

plt.grid(True)

plt.show()