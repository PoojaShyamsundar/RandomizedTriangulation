import random
from random import randint
import matplotlib.pyplot as plot
from operator import itemgetter
from functools import partial
import numpy as npy
from itertools import islice

def uniform_triangle(u, v):
    while True:
        x = random.random()
        y = random.random()
        withinTir = x + y <= 1
        point = x * u + y * v if withinTir else (1 - x) * u + (1 - y) * v
        yield point


triangleGen = npy.array([
            [1, 2],
            [3, 8],
            [7, 5],
        ])

it = uniform_triangle(
    triangleGen[1] - triangleGen[0],
    triangleGen[2] - triangleGen[0],
        )

pts = npy.array(list(islice(it, 0, 8)))
pts += triangleGen[0]
fig, ax = plot.subplots()
ax.scatter(pts[:, 0], pts[:, 1], s=1)
fig.savefig("triangle.png", dpi=200)

def clockwise(points):
    #give points in clockwise direction to experiment.
    port = npy.array(min(points, key=itemgetter(0)))
    starbrd = npy.array(max(points, key=itemgetter(0)))
    basis = starbrd - port                           # the new basis vector
    ref = npy.cross(basis, port)                  # check top and bottom
    proj = [npy.cross(basis, p) for p in points]
    top = [p for p,b in zip(points, proj) if b >= ref]
    below = [p for p,b in zip(points, proj) if b < ref]

    yield from sorted(top, key=partial(npy.dot, basis))
    yield from sorted(below, key=partial(npy.dot, basis), reverse=True)

n = 40
X = [randint(0, 20) for _ in range(n)]
Y = [randint(0, 20) for _ in range(n)]
rand_points = pts

poly = rand_points
X, Y = zip(*poly)

with plot.style.context('lhk'):
     plot.subplots(figsize=(30, 10))
     plot.plot(X, Y)
     print("these points ");
     for ix, p in enumerate(poly):
      plot.annotate(ix, p)
     plot.show()