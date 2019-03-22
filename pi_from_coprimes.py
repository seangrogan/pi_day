from math import gcd, sqrt, pi
import argparse, time
try:
    from numpy.random import randint as rnd
except ImportError:
    from random import randint as rnd


def _pi():
    return sqrt(6/(sum([1 if 1 == gcd(rnd(1, arg_parse().m_int), rnd(1, arg_parse().m_int)) else 0 for i in range(arg_parse().n)])/arg_parse().n))


def pi_from_coprimes():
    t=time.time()
    args = arg_parse()
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


def arg_parse():
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
    pi_from_coprimes()
else:
    pass
