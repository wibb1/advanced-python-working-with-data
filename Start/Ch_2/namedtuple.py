# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")

p1 = Point(10,20)
p2 = Point(30,40)

print(p1, p2) # prints in a readable format
print(p1.x, p1.y) # still able to access the values individually


# TODO: use _replace to create a new instance

p1 = p1._replace(x=100) # replace an individual element of the tuple
print(p1)