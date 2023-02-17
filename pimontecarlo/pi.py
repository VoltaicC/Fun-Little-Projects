import matplotlib.pyplot as plt
import random
import math

x = 0
y = 0
inside = 0
#number of points to graph
dots = 100000

plt.axis([0, 2, 0, 2])
fig = plt.gcf()
ax = fig.gca()
circle = plt.Circle((1, 1), 1, color='blue', fill=False)
for i in range(dots):
    x = random.random() * 2
    y = random.random() * 2
    point = (x, y)
    center = (1,1)
    distance = math.dist(point, center)

    if(distance > 1):
        plt.plot(x, y, 'ro', markersize=5, color="red",)
    else:
        plt.plot(x, y, 'ro', markersize=5, color="green")
        inside += 1

pi = 4 * (inside/dots)

ax.add_patch(circle)
plt.title(pi)
plt.show()
