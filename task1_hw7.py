import math
import re

def ball_collide(b1, b2):
    """
    This method accepts two tuples, and unpacks them as thus
    (x, y, z, r)

    It then calculates if these two spheres collide and returns a True or False
    depending on if they are colliding or not
    """

    (x1, y1, z1, r1) = b1
    (x2, y2, z2, r2) = b2

    distance = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2))
    radius = r1+r2

    if (distance > radius):
        return False
    else:
        return True

#main
f = open("/home/lrowe/submit/files/balltest.txt", "r")
for line in f:
    data = re.split(":|,", line)
    b1 = (float(data[0]), float(data[1]), float(data[2]), float(data[3]))
    b2 = (float(data[4]), float(data[5]), float(data[6]), float(data[7]))
    if (ball_collide(b1, b2) == True):
        print("Collision!")
    else:
        print("No collision.")
