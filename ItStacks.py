import numpy as np
import matplotlib.pyplot as plt

n = 400
layers = 10  # Number of layers for the ladder

x = np.linspace(-5, 5, n)
y = np.linspace(-5, 5, n)
z_offsets = np.linspace(0, 10, layers)  # Offset for each layer

xm, ym = np.meshgrid(x, y)

# Define the equation for the triangle
z1 = 5 * ym - xm
z2 = 10 * ym - xm
z3 = 2 * xm

# Function to create cross-section
def create_cross_section(xm, ym, z1, z2, z3):
    cross_section = np.zeros_like(z1, dtype=bool)
    for i in range(z1.shape[0]):
        for j in range(z1.shape[1]):
            if z1[i, j] > 0 and z2[i, j] > 0 and z3[i, j] > 0:
                cross_section[i, j] = True
    return cross_section

# Generate cross-section
slice_1 = create_cross_section(xm, ym, z1, z2, z3)

# Plotting the 3D ladder
fig = plt.figure('3D Ladder', figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

for z_offset in z_offsets:
    # Masked array to plot only the valid parts of the triangle
    z_masked = np.ma.masked_where(~slice_1, np.full_like(slice_1, z_offset, dtype=float))
    ax.plot_surface(xm, ym, z_masked, color='black', alpha=0.7, rstride=1, cstride=1)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Ladder Structure')
plt.show()
