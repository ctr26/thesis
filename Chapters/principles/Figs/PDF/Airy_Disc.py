#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:41:37 2018

@author: craggles
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import scipy.special
import sklearn

from matplotlib import cm
from matplotlib import rc
import matplotlib

matplotlib.rc('pdf', fonttype=42)

start = -10
end = 10
resolution = 512

x=y= np.linspace(start,end,num=resolution)
xx,yy = np.meshgrid(x,y)

rr = np.sqrt(xx**2+yy**2)
tt = np.arctan2(y,x)

airy = 2*np.divide(scipy.special.jve(1,rr),rr)
#norm_airy = sklearn.preprocessing.normalize(airy)

#plt.imshow(airy)

colors = cm.viridis(airy)

fig = plt.figure()


#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#pgf_with_rc_fonts = {"pgf.texsystem": "pdflatex"}
#matplotlib.rcParams.update(pgf_with_rc_fonts)

ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([start, end])
ax.set_ylim3d([start, end])
ax.set_zlim3d([-0.08, 1])
# Plot a basic wireframe.
#ax.plot_wireframe(xx, yy, airy, rstride=10, cstride=10)

#surf = ax.plot_surface(xx, yy, airy, rcount=50, ccount=50,
#                       facecolors=colors, shade=False)

surf = ax.plot_surface(xx, yy, airy, cmap=cm.viridis)
#surf.set_facecolor((0,0,0,0))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Electric field')
plt.tight_layout()

plt.savefig("airy_E_fill.pdf")
surf.remove()

#plt.show()
#%%
#plt.cla()
surf = ax.plot_surface(xx, yy, airy**2, cmap=cm.viridis)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Intensity')
plt.savefig("airy_I_fill.pdf")
plt.show()