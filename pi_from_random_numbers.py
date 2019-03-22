try:
    from numpy.random import random as rnd
    from numpy import sqrt
except ImportError:
    from random import random as rnd
    from math import sqrt
""" 
Estimates the value of Pi by randomly picking two (pseudo) random real 
(floating point) numbers in the range of [0.0, 1.0[.  The two random numbers 
are then considered a point [x,y].  It then tests if the point is within one
unit of the origin.  The ratio of the number of points inside to total points 
should tend to pi over several thousand iterations.  A test execution showing 
this is at the end of the script.  
"""


def pi(**kwargs):
    """ Computes pi with random points
    :param n:
    :return:
    """
    return 4 * sum(
        [1 if (sqrt(rnd() ** 2 + rnd() ** 2) <= 1)
         else 0
         for k in range(kwargs.get('n', 100))]
    ) / kwargs.get('n', 100)


if __name__ == "__main__":
    print(pi(n=10000))
