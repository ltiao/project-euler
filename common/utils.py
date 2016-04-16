from itertools import chain, combinations, count, islice
from collections import Counter, defaultdict
from six.moves import map, range, reduce

def prime_factors(n):
    if n < 1:
        raise ValueError('Requires positive nonzero integer')
    else:
        prime_factors_ = Counter()

        if n == 1:
            return prime_factors_

        for p in prime_range(int(n**0.5) + 1):
            while n % p == 0:
                prime_factors_[p] += 1
                n /= p
        if n > 1:  # n has no further prime factors
            prime_factors_[n] = 1
        return prime_factors_


def _prime_sieve_eratosthenes_2():
    factors = defaultdict(set)
    for n in count(2):
        if factors[n]:
            for m in factors.pop(n):
                factors[n+m].add(m)
        else:
            factors[n*n].add(n)
            yield n


def _prime_sieve_eratosthenes_1(n):
    composites = set()
    for i in range(2, n):
        if i not in composites:
            yield i
            composites.update(set(range(i*i, n, i)))


def prime_range(end, start=2):
    return (p for p in _prime_sieve_eratosthenes_1(end) if p >= start)


reconstruct = lambda c: reduce(lambda x, y: x*y, map(lambda x: x**c[x], c))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
