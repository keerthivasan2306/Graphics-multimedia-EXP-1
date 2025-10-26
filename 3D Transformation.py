import numpy as np
import matplotlib.pyplot as plt
cube = np.array([
    [0,0,0],[1,0,0],[1,1,0],[0,1,0],
    [0,0,1],[1,0,1],[1,1,1],[0,1,1]
])
def translate(vertices, tx, ty, tz):
    """Move shape by tx, ty, tz"""
    return vertices + [tx, ty, tz]
def scale(vertices, sx, sy, sz):
    """Scale shape by sx, sy, sz"""
    return vertices * [sx, sy, sz]
def rotate_z(vertices, angle_deg):
    """Rotate shape around Z-axis by angle_deg degrees"""
    rad = np.radians(angle_deg)
    R = np.array([[np.cos(rad), -np.sin(rad),0],
                  [np.sin(rad),  np.cos(rad),0],
                  [0,0,1]])
    return vertices @ R.T

cube_translated = translate(cube, 2, 1, 0)
cube_scaled     = scale(cube_translated, 2, 1.5, 1)
cube_rotated    = rotate_z(cube_scaled, 45)

edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
         (0,4),(1,5),(2,6),(3,7)]

def plot_cube(vertices, label):
    for i,j in edges:
        plt.plot([vertices[i,0], vertices[j,0]],
                 [vertices[i,1], vertices[j,1]], color="black")

    x, y = vertices[0,0], vertices[0,1]
    plt.text(x, y, label, fontsize=10, fontweight='bold')

plt.figure(figsize=(6,6))
plot_cube(cube, "Original Cube")
plot_cube(cube_translated, "Translated")
plot_cube(cube_scaled, "Scaled")
plot_cube(cube_rotated, "Rotated")

plt.title("2D Representation of 3D Transformations")
plt.xlabel("X-axis"); plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
