"""
Src:https://pypi.python.org/pypi/numpy-stl

"""

from mpl_toolkits import mplot3d
from matplotlib import pyplot
from stl import mesh
import numpy as np
############################################# INPUT ####################################################################
# Load the STL files and add the vectors to the plot
#your_mesh2 = mesh.Mesh.from_file('../STLFiles/test2.stl')
your_mesh2 = mesh.Mesh.from_file('../STLFiles/cylinder_sphereA.stl')

train_array = [np.append(your_mesh2.data[0][0],your_mesh2.data[0][1])]

for i in range(1,your_mesh2.data.size):
    train_array = np.concatenate((train_array,[np.append(your_mesh2.data[i][0],your_mesh2.data[i][1])]))

print(train_array[0])
print(train_array.shape[0])
print(train_array.shape)
#print(your_mesh3.data[117])

############################################# OUTPUT ###################################################################
data = np.zeros(train_array.shape[0], dtype=mesh.Mesh.dtype)

for i in range(train_array.shape[0]):
    data['vectors'][i] = np.array([[train_array[i][3], train_array[i][4], train_array[i][5]],
                                   [train_array[i][6], train_array[i][7], train_array[i][8]],
                                   [train_array[i][9], train_array[i][10], train_array[i][11]]])

#print(data['vectors'])

new_mesh = mesh.Mesh(data.copy())
print(new_mesh)
new_mesh.save('new_stl_file.stl', mode=1)

