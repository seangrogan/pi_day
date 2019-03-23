try:
    from numpy.random import random as rnd
    from numpy import sqrt
except ImportError:
    from random import random as rnd
    from math import sqrt
import time

""" 
Estimates the value of Pi by randomly picking two random real (floating point) 
numbers in the range of [0.0, 1.0[. The two random numbers are then considered 
a point [x,y].  It then tests if the point is within one unit of the origin.  
The ratio of the number of points inside to total points should tend to pi over 
several thousand iterations.  A test execution showing this is at the end of 
the script.  
"""


def pi(n=100):
    return 4 * sum((rnd() ** 2 + rnd() ** 2 <= 1) for _ in range(n)) / n


if __name__ == "__main__":
    sims = 10000000
    print('n:', sims)
    t1 = time.time()
    print('pi:', pi(n=sims))
    t2 = time.time()
    print('t:', t2 - t1)
