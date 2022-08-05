
import numpy as np


def Approx_triang(setpoints, n):
    print("arc")
    print(setpoints)
    if len(setpoints) < 3: return []
    #If triangle is not found
    if n == 0: return Approx_triang(list(reversed(setpoints)), len(setpoints))
    a, b, c = setpoints[:3]
    p, q = b-a, c-a
    cross_z = p[0] * q[1] - p[1] * q[0]
    if cross_z >= 0: setpoints.pop(1)
    setpoints.append(setpoints.pop(0))

    # cover using recursion
    if cross_z > 0: return [ (a, b, c) ] + Approx_triang(setpoints, len(setpoints))
    else: return Approx_triang(setpoints, n - 1)


def Approx_triang(setOfPoints):
    '''Randomized approach to triangulation works in n order because it takes three points and connects and removes.
    '''
    setOfPoints = list(setOfPoints)
    n = len(setOfPoints)
    if n > 0 and type(setOfPoints[0]) is not np.ndarray:
        setOfPoints = [np.array(x) for x in setOfPoints]
    return Approx_triang(setOfPoints, n)
