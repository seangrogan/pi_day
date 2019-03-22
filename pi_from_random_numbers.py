try:
    from numpy.random import random as rnd
    from numpy import sqrt
except ImportError:
    from random import random as rnd
    from math import sqrt
import time

""" 
Estimates the value of Pi by randomly picking two (pseudo) random real 
(floating point) numbers in the range of [0.0, 1.0[.  The two random numbers 
are then considered a point [x,y].  It then tests if the point is within one
unit of the origin.  The ratio of the number of points inside to total points 
should tend to pi over several thousand iterations.  A test execution showing 
this is at the end of the script.  
"""


def pi(n=100):
    """ Computes pi with random points
    :param n:
    :return:
    """
    return 4 * sum([1 for i in range(n) if (sqrt(rnd() ** 2 + rnd() ** 2) <= 1)]) / n


if __name__ == "__main__":
    n = 1000
    t1 = time.time()
    print(pi(n=n))
    t2 = time.time()
