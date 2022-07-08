import numpy as np
x = np.linspace(1,10,10)
y = np.linspace(11,20,10)
X,Y = np.meshgrid(x,y)
X
Y

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.grid()
x1,y1 = np.meshgrid(x,y)
x2,y2 = np.meshigrid(x,y,indexing='ij')

print(x1[0][1], x2[0][1])

x2,y2 = np.meshgrid(x,y,sparse=True)
x2
x2.shape
y2
