import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
#Try out for a x,y bound vs say a circle.
x1 = 4
x2 = 1
x3 = 7
y1 = 1
y2 = 7
pts = np.array([[x1,y1], [x2,y2], [x3,np.sqrt(y2**2 - y1**2)]])
p = Polygon(pts, closed=False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()