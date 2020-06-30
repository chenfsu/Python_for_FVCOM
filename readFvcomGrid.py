from numpy import loadtxt
import numpy as np

def readFvcomGrid(filename,nodeNum,cellNum):
    # filename is fvcom_grd.dat (input)
    # nodeNum (input)
    # cellNum (input)
    # x is x coordinates (output)
    # y is y coordinates (output)
    # triangles (output)
    # Example: ax1.triplot(x, y, triangles, 'go-', lw=1.0)
    triTemp = loadtxt(filename, comments="#", usecols=(1,2,3),skiprows=2,max_rows=cellNum,unpack=False)
    znode = loadtxt(filename, comments="#", usecols=(1,2),skiprows=2+cellNum,max_rows=nodeNum,unpack=False)
    x=np.asarray(znode[:,0])# node x
    y=np.asarray(znode[:,1])# node y
    triangles=np.asarray(triTemp)-1
    return x,y,triangles




