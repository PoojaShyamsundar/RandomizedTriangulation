
import numpy as np
import matplotlib.pyplot as plt
from src.cover import Approx_triang
from datetime import datetime


def unzip(x):
    return np.array(x).T


def to_array(arc):
    return [ np.array(p) for p in arc ]


def otherShape():
    arc = [ [0,0], [1,0], [2,0],
        [3,0], [2,3], [1,2], [1,3],
        [0,3], [0,2], [-1,2], [-1,3], [-2,3],
        [-2,0], [-1,0], [-1,1], [0,1] ]
    return to_array( arc )


def triang():
    arc = [      [2.50057207, 2.81978219] ,       [2.53202349, 4.28683814] ,       [3.0, 6.0] ,       [3.44812743, 6.87582195] ,       [4.38987054, 6.85825276] ,       [5.45956031, 5.63164632] ,       [4.40076023, 3.70893737] ,       [3.51589753, 3.47164788] ]

    return to_array(arc)

def tryShape():
    arc = [ [0,0], [2,0], [1,3],
        [2,5], [0,5], [0,2], [1,1], [0,1] ]
    return to_array( arc )


def connectPoints(arc, ax, plot_trigles=True):
    ax.plot(*unzip(arc + arc[:1]), '#bbbbab', linewidth=5)

    tgles = Approx_triang(arc)

    if plot_trigles:
        for tri in tgles:
            ax.plot(*unzip(tri + tri[:1]))


if __name__ == '__main__':
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    plot_tris = True
    uniform_fill = True
    fig, axs = plt.subplots( 1, 2, figsize=(16,6) )
    connectPoints(triang(), axs[0], plot_tris)
    plt.show()
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

