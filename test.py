import math as m

import pi_from_coprimes as pfc
import pi_from_random_numbers as pfr

print('pi_from_coprimes       : {}'.format(pfc.pi(n=1000000, max_int=50000)))
print('pi_from_random_numbers : {}'.format(pfr.pi(n=1000000)))
print('pi from math           : {}'.format(m.pi))
