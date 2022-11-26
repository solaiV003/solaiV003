import matplotlib.pyplot as plt
import numpy as np
#1
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, 'o:r', ls = '--')
plt.title("naanga kolaaru")
plt.show()
#2
plt.plot(xpoints,ypoints,'o', ms=20, mec='r')
plt.grid(color='red',ls='--',linewidth=0.5)
plt.show()
#3
y = np.array([2,3,5,6,7])
plt.plot(y,linewidth = '20')
plt.show()
#4
plt.plot(y,ls = ':', marker = '*')
plt.title("kolaaru graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#5
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1,ls=':')
plt.plot(y2,ls='--')

plt.show()
#6
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y,'o:r')

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y,'o:g')

plt.show()

