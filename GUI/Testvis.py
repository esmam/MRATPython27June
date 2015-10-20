dates = [20110101,20110104,20110105,20110106,20110107,20110108,20110111,20110112]

zAxis0= [       0,       0,       0,       0,       0,       0,       0,       0]
Actual= [    1132,    1184,    1177,     950,    1066,    1098,    1116,    1211]

zAxis1= [       1,       1,       1,       1,       1,       1,       1,       1]
Tops1 = [    1156,    1250,    1156,    1187,    1187,    1187,    1156,    1156]
Mids1 = [    1125,    1187,    1125,    1156,    1156,    1156,    1140,    1140]
Lows1 = [    1093,    1125,    1093,    1125,    1125,    1125,    1125,    1125]

zAxis2= [       2,       2,       2,       2,       2,       2,       2,       2]
Tops2 = [    1125,    1125,    1125,    1125,    1125,    1250,    1062,    1250]
Mids2 = [    1062,    1062,    1062,    1062,    1062,    1125,    1000,    1125]
Lows2 = [    1000,    1000,    1000,    1000,    1000,    1000,     937,    1000]

zAxis3= [       3,       3,       3,       3,       3,       3,       3,       3]
Tops3 = [    1250,    1250,    1250,    1250,    1250,    1250,    1250,    1250]
Mids3 = [    1187,    1187,    1187,    1187,    1187,    1187,    1187,    1187]
Lows3 = [    1125,    1125,    1000,    1125,    1125,    1093,    1093,    1000]

import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = matplotlib.pyplot.figure()
ax  = fig.add_subplot(111, projection = '3d')

#actual values
ax.scatter(dates, zAxis0, Actual, color = 'c', marker = 'o')

#Upper limits, Lower limts, and Mid-range for the FIRST plane
ax.plot(dates, zAxis1, Tops1, color = 'r')
ax.plot(dates, zAxis1, Mids1, color = 'y')
ax.plot(dates, zAxis1, Lows1, color = 'b')

#Upper limits, Lower limts, and Mid-range for the SECOND plane
ax.plot(dates, zAxis2, Tops2, color = 'r')
ax.plot(dates, zAxis2, Mids2, color = 'y')
ax.plot(dates, zAxis2, Lows2, color = 'b')

#Upper limits, Lower limts, and Mid-range for the THIRD plane
ax.plot(dates, zAxis3, Tops3, color = 'r')
ax.plot(dates, zAxis3, Mids3, color = 'y')
ax.plot(dates, zAxis3, Lows3, color = 'b')

#These two lines are just dummy data that plots transparent circles that
#occpuy the "wall" behind my actual plots, so that the last plane appears
#floating in 3D rather than being pasted to the plot's background
zAxis4= [       4,       4,       4,       4,       4,       4,       4,       4]
ax.scatter(dates, zAxis4, Actual, color = 'w', marker = 'o', alpha=0)

matplotlib.pyplot.show()