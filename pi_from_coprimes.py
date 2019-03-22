from math import gcd, sqrt, pi
import argparse, time
try:
    from numpy.random import randint as rnd
except ImportError:
    from random import randint as rnd


def pi(**kwargs):
    """ Computes pi with coprimes.
    :param max_int: upper bound of the random integers
    :param n: gets the number of trials to execute
    :return: Estimate of pi
    """
    return sqrt(6 / (sum(
        [1 if 1 == gcd(rnd(1, kwargs.get('max_int', default=120)), rnd(1, kwargs.get('max_int', default=120)))
         else 0
         for i in range(kwargs.get('n', default=500))]
    ) / kwargs.get('n', default=500)))


def _pi_from_coprimes():
    """ Does an experiment to calculate pi with coprimes
    """
    t=time.time()
    args = _arg_parse()
    cp_count = sum([1 if 1 == gcd(rnd(1, args.m_int), rnd(1, args.m_int))
                    else 0
                    for i in range(args.n)])
    pi_estimate = sqrt(6/(cp_count/args.n))
    print('Coprime Count  \t{c} of {n} ({pct:.2%})'.format(c=cp_count,
                                                           n=args.n,
                                                           pct=(cp_count/args.n)
                                                           ))
    print('π Estimate     \t{}'.format(pi_estimate))
    print('Pct Difference \t{pct:.2%}'.format(pct=(pi_estimate-pi)/(pi_estimate+pi)))
    print('Time           \t{:.2f} sec'.format(time.time()-t))


def _arg_parse():
    parser = argparse.ArgumentParser(description='Calculate π using coprimes')
    parser.add_argument('-n',
                        type=int,
                        help='Number of trials, default=500',
                        default=500)
    parser.add_argument('-m_int', '-max_int','-m',
                        type=int,
                        help='Maximum Random Integer, default=120',
                        default=120)
    return parser.parse_args()


if __name__ == '__main__':
    _pi_from_coprimes()
else:
    pass
