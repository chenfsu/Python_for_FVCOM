import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import local

nodeNum = 20587
cellNum = 40954
filename = "negoms_grd.dat"

x,y,triangles = local.readFvcomGrid(filename,nodeNum,cellNum)





fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
#ax1.triplot(x, y, triangles, 'go-', lw=1.0)
ax1.triplot(x, y, triangles, 'b-', lw=1)
ax1.set_title('triplot of user-specified triangulation')
ax1.set_xlabel('Longitude (degrees)')
ax1.set_ylabel('Latitude (degrees)')

#plt.show()

fig1.savefig('./'+filename+'.png',dpi=400)
plt.close()






