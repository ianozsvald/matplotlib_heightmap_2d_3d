"""Build a 3 dimensional plot of the cross entropy function"""
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

Axes3D.zorder  # stop annoying pyflake warning

def three_parts():
    """return 3 numbers that sum to 1.0"""
    v1 = random.randint(0, 1000)
    v2 = random.randint(0, 1000)
    v3 = random.randint(0, 1000)
    total = float(v1+v2+v3)
    return v1/total, v2/total, v3/total

xs = []
ys = []
zs = []
cross_entropies = []
for n in range(5000):
    x, y, z = three_parts()
    xs.append(x)
    ys.append(y)
    zs.append(z)
    cross_entropy = -(x * np.log2(x) + y * np.log2(y) + z * np.log2(z))
    cross_entropies.append(cross_entropy)

f = plt.figure(0)
f.clf()
ax = f.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c=cross_entropies)
ax.set_xlabel('P(X)')
ax.set_ylabel('P(Y)')
ax.set_zlabel('P(Z)')
plt.xlim(0, 1)
plt.ylim(0, 1)
ax.set_zlim(0, 1)
plt.title("Cross Entropies for 3 variables (where x+y+z==1)")
# Show the image
plt.show()
