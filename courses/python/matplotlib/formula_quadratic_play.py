# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import math

# Create the vectors X and Y
#x = np.array(range(10))
x = np.array(range(-100, 100))
y = 1 / (1 - x) 

# Create the plot
plt.plot(x,y,label='y = x**3')

# Add a title
plt.title('Playground formula')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
