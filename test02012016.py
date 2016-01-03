"""
Src:https://pypi.python.org/pypi/numpy-stl

"""

from mpl_toolkits import mplot3d
from matplotlib import pyplot
from stl import mesh
import numpy as np

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh3 = mesh.Mesh.from_file('STLFiles/cylinder_sphereB.stl')
your_mesh2 = mesh.Mesh.from_file('STLFiles/test2.stl')
your_mesh = mesh.Mesh.from_file('STLFiles/test.stl')
"""
print("vectors")
print(your_mesh.vectors)
print("normals")
print(your_mesh.normals)
print("name")
print(your_mesh.name)
print("data")
print(your_mesh.data)
print("points")
print(your_mesh.points)
print("attr")
print(your_mesh.attr)
"""

train_array = np.array([])

train_array = [np.append(your_mesh2.data[0][0],your_mesh2.data[0][1])]

for i in range(1,your_mesh2.data.size):
    train_array = np.concatenate((train_array,[np.append(your_mesh2.data[i][0],your_mesh2.data[i][1])]))

print(train_array)


