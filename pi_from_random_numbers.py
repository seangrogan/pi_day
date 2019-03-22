import random
import math

""" 
Estimates the value of Pi by randomly picking two (pseudo) random real 
(floating point) numbers in the range of [0.0, 1.0[.  The two random numbers 
are then considered a point [x,y].  It then tests if the point is within one
unit of the origin.  The ratio of the number of points inside to total points 
should tend to pi over several thousand iterations.  A test execution showing 
this is at the end of the script.  
"""
def pi_estimator(n):
    inside = 0
    inside = sum([1 if inside_circle() else 0 for k in range(n)])
    return 4*inside/n


def inside_circle():
    # Returns True if the point is inside the circle.
    return math.sqrt(random.random() ** 2 + random.random() ** 2) <= 1

if __name__ == "__main__":
    n1 = 10
    n2 = 100
    n3 = 10000
    n4 = 1000000
    print("Estimating Pi")
    print("-------------------------------------------------------")
    p1 = pi_estimator(n1)
    print("After",n1,"iterations, we estimate pi to be",p1)
    print("In python, Pi is estimated as", math.pi)
    print("The percent difference is", int(((p1 - math.pi)/math.pi)*100),"%")
    print("-------------------------------------------------------")
    p2 = pi_estimator(n2)
    print("After",n2,"iterations, we estimate pi to be",p2)
    print("In python, Pi is estimated as", math.pi)
    print("The percent difference is", int(((p2 - math.pi)/math.pi)*100), "%")
    print("-------------------------------------------------------")
    p3 = pi_estimator(n3)
    print("After",n3,"iterations, we estimate pi to be",p3)
    print("In python, Pi is estimated as", math.pi)
    print("The percent difference is", int(((p3 - math.pi)/math.pi)*1000)/10.0, "%")
    print("-------------------------------------------------------")
    p4 = pi_estimator(n4)
    print("After",n4,"iterations, we estimate pi to be",p4)
    print("In python, Pi is estimated as", math.pi)
    print("The percent difference is", int(((p4 - math.pi)/math.pi)*1000)/10.0, "%")
