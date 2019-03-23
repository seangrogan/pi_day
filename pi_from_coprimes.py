import argparse, time

try:
    from numpy.random import randint as rnd
    from numpy import gcd, sqrt, pi as pie
except ImportError:
    from random import randint as rnd
    from math import gcd, sqrt, pi as pie


def pi(max_int=256 ** (2 * 36), n=500):
    return sqrt(6 / (sum(1 == gcd(rnd(1, max_int), rnd(1, max_int)) for _ in range(n)) / n))


def pi_from_coprimes():
    """ Does an experiment to calculate pi with coprimes
    """
    t = time.time()
    args = _arg_parse()
    cp_count = sum((1 == gcd(rnd(1, args.m_int), rnd(1, args.m_int))) for _ in range(args.n))
    pi_estimate = sqrt(6 / (cp_count / args.n))
    print('Coprime Count  \t{c} of {n} ({pct:.2%})  '.format(c=cp_count, n=args.n, pct=(cp_count / args.n)))
    print('π Estimate     \t{}                      '.format(pi_estimate))
    print('Pct Difference \t{pct:.2%}               '.format(pct=(pi_estimate - pie) / (pi_estimate + pie)))
    print('Time           \t{:.2f} sec              '.format(time.time() - t))


def _arg_parse():
    parser = argparse.ArgumentParser(description='Calculate π using coprimes')
    parser.add_argument('-n',
                        type=int,
                        help='Number of trials, default=500',
                        default=500)
    parser.add_argument('-m_int', '-max_int', '-m',
                        type=int,
                        help='Maximum Random Integer, default=120',
                        default=120)
    return parser.parse_args()


if __name__ == '__main__':
    pi_from_coprimes()
else:
    pass
