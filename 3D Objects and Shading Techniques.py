import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define cube vertices
vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
])

# Define 6 faces of the cube
faces = [
    [vertices[j] for j in [0, 1, 2, 3]],  # bottom
    [vertices[j] for j in [4, 5, 6, 7]],  # top
    [vertices[j] for j in [0, 1, 5, 4]],  # front
    [vertices[j] for j in [2, 3, 7, 6]],  # back
    [vertices[j] for j in [1, 2, 6, 5]],  # right
    [vertices[j] for j in [4, 7, 3, 0]]   # left
]

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'orange']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create and add the 3D polygon collection
poly3d = Poly3DCollection(faces, facecolors=colors, edgecolors='black', linewidths=1, alpha=0.9)
ax.add_collection3d(poly3d)

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Cube with Flat Shading')

# Set equal aspect ratio and axis limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_box_aspect([1, 1, 1])  # Equal aspect for all axes

plt.show()
