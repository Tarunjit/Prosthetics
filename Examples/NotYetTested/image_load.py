import matplotlib.pyplot as plt
from scipy import misc 

f=misc.imread('depth_map_z087.png', flatten =1)

print f.shape

f[0,40]

plt.imshow(f)
plt.show()


