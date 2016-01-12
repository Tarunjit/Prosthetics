"""
Src:https://pypi.python.org/pypi/numpy-stl

"""

from mpl_toolkits import mplot3d
from matplotlib import pyplot
from stl import mesh
import numpy as np

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
############################################# INPUT ####################################################################
# Load the STL files and add the vectors to the plot
#your_mesh2 = mesh.Mesh.from_file('../STLFiles/test2.stl')

# need to do ravelling - it is required
your_mesh = mesh.Mesh.from_file('./STLFiles/cylinder_sphereA.stl')
your_mesh2 = mesh.Mesh.from_file('./STLFiles/cylinder_sphereA_offset.stl')
your_mesh3 = mesh.Mesh.from_file('./STLFiles/cylinder_sphereB_offset.stl')

X_train_array = [np.append(your_mesh.data[0][0], your_mesh.data[0][1])]
Y_train_array = [np.append(your_mesh2.data[0][0], your_mesh2.data[0][1])]
X_test_array = [np.append(your_mesh3.data[0][0], your_mesh3.data[0][1])]

for i in range(1,your_mesh.data.size):
    X_train_array = np.concatenate((X_train_array, [np.append(your_mesh.data[i][0], your_mesh.data[i][1])]))

for i in range(1,your_mesh.data.size):
    Y_train_array = np.concatenate((Y_train_array, [np.append(your_mesh2.data[i][0], your_mesh2.data[i][1])]))

for i in range(1,your_mesh.data.size):
    X_test_array = np.concatenate((X_test_array, [np.append(your_mesh3.data[i][0], your_mesh3.data[i][1])]))


print(X_train_array.ravel())
#print(Y_train_array.shape)
#print(X_test_array.shape)
#print(your_mesh3.data[117])
############################################# ML ###################################################################

# Fit estimators
ESTIMATORS = {
    #"Extra trees": ExtraTreesRegressor(n_estimators=10, max_features=32,
                                       #random_state=0)#,
    #"K-nn": KNeighborsRegressor()#,
    #"Linear regression": LinearRegression()#,
    "Ridge": RidgeCV()#,
}

#y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train_array, Y_train_array)
    y_test_predict = estimator.predict(X_test_array)

print(y_test_predict.shape)
############################################# OUTPUT ###################################################################

# define unravelling logic - required

data = np.zeros(y_test_predict.shape[0], dtype=mesh.Mesh.dtype)

for i in range(y_test_predict.shape[0]):
    data['vectors'][i] = np.array([[y_test_predict[i][3], y_test_predict[i][4], y_test_predict[i][5]],
                                   [y_test_predict[i][6], y_test_predict[i][7], y_test_predict[i][8]],
                                   [y_test_predict[i][9], y_test_predict[i][10], y_test_predict[i][11]]])

#print(data['vectors'])

new_mesh = mesh.Mesh(data.copy())
print(new_mesh)
new_mesh.save('new_stl_file.stl', mode=1)

