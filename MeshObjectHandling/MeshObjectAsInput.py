"""
Src: https://pypi.python.org/pypi/numpy-stl

"""

from mpl_toolkits import mplot3d
from matplotlib import pyplot
from stl import mesh
import numpy as np

# Load the STL files and add the vectors to the plot
your_mesh3 = mesh.Mesh.from_file('../STLFiles/cylinder_sphereB.stl')

train_array = [np.append(your_mesh3.data[0][0],your_mesh3.data[0][1])]

for i in range(1,your_mesh3.data.size):
    train_array = np.concatenate((train_array,[np.append(your_mesh3.data[i][0],your_mesh3.data[i][1])]))

#print(train_array[117])
#print(your_mesh3.data[117])




