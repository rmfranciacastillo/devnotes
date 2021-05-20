import numpy as np
import matplotlib.pyplot as plt

xv = np.array([0, 1, 2, 3, 4])
yv = np.zeros(len(xv))


print('--------------')
print('x      |    y  ')
print('--------------')
for i in range(len(xv)):
    yv[i] = np.sqrt(xv[i])
    print('{:5.2f}  | {:5.2f}'.format(xv[i],yv[i]))

print('--------------')


xv = np.linspace(0, 4, 50) # Generates 30 points between 0 and 4
yv = np.sqrt(xv)  # Vector evaluation, sqrt() is applied to each point in xv

plt.plot(xv, yv, 'r-o')
plt.show()
