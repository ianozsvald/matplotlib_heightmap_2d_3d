"""Build a trivial 3x3 grid, plot as a surface"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Build a 5x3 grid
Xr = np.arange(5)
Yr = np.arange(3)
X, Y = np.meshgrid(Xr, Yr)

# Create heights in the grid
Z = np.zeros(X.shape)
Z[1][1] = 1
Z[1][2] = 2
Z[1][3] = 5
Z[2][1] = 1

# Build a figure with 2 subplots, the first is 3D
fig = plt.figure()
fig.suptitle("3D and 2D heighmap")
ax = fig.add_subplot(2, 1, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)

ax2 = fig.add_subplot(2, 1, 2)
im = ax2.imshow(Z, cmap='hot', interpolation='nearest')
# swap the Y axis so it aligns with the 3D plot
ax2.invert_yaxis()
# add an explanatory colour bar
plt.colorbar(im, orientation='horizontal')

# Show the image
plt.show()
