import matplotlib.pyplot as plt
import random
import numpy as np

#Gives an X and Y coordinate to the 3 starting points: a, b, and c
ax = 1
ay = 1

bx = 2
by = 3

cx = 3
cy = 1

#Plots the 3 starting points.
plt.plot([ax, bx, cx], [ay, by, cy], 'ro')

#sets the size of the plot
plt.axis([0, 4, 0, 4])

#coordinates for a random starting point
pointx = 4
pointy = 1.5

#plots starting point
plt.plot(pointx, pointy, 'ro')

#plots points halfway between the last point plotted and either a, b, or c (randomly)
for i in range(50):
    #pick random corner
    corner = random.randint(1, 3)
    #assign an x and y based on the corner
    if corner == 1:
        cornerx = ax
        cornery = ay
    elif corner == 2:
        cornerx = bx
        cornery = by
    else:
        cornerx = cx
        cornery = cy
    #midpoint formula 
    pointx = (pointx + cornerx) / 2
    pointy = (pointy + cornery) / 2
    #plots the random point
    plt.plot(pointx, pointy, 'ro', markersize=1)
    #uncomment this to see them get plotted in real time
    #plt.pause(0.0001)

plt.show()