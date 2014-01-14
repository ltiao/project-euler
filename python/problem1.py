from itertools import chain, combinations

def powerset_generator(iterable):
    for subset in chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1)):
        yield subset
        
# possibly combine all_products and coefficients rather than zipping them at a later stage
def all_products(iterable):
    for subset in powerset_generator(iterable):
        if subset:
            yield reduce(lambda x, y: x*y, subset)

# set inclusion/exclusion principle
def coefficients(iterable):
    for subset in powerset_generator(iterable):
        if subset:
            # bit shift rather than exponentiation
            # for efficiently getting signs
            yield 2*(len(subset)&1)-1

def simultaneous_sum_multiple(iterable, n):
    # Need remove elements of iterable that
    # are multiples of other elements. i.e. 
    # all elements of iterable must be relatively
    # coprime
    return reduce(lambda x, y: x+y[0]*sum_multiple(y[1], n), zip(coefficients(iterable), all_products(iterable)), 0)

# higher-order function
def simultaneous_sum_multiple_func(iterable):
    # Need remove elements of iterable that
    # are multiples of other elements. i.e. 
    # all elements of iterable must be relatively
    # coprime
    return lambda n: reduce(lambda x, y: x+y[0]*sum_multiple(y[1], n), zip(coefficients(iterable), all_products(iterable)), 0)

def sum_multiple(k, n):
    """Return the sum of all positive integer 
    multiples of k less than or equal to n,
    i.e. sum_multiple(k, n) = k + 2k + ... + k floor(n/k)
    
    >>> sum_multiple(1, 10)
    55
    >>> sum_multiple(3, 10)
    18
    >>> sum_multiple(3, 9)
    18
    """
    N = n/k
    return k*N*(N+1)/2

if __name__ == "__main__":    
    import doctest
    doctest.testmod()
    
    print sum_multiple(3, 999) + sum_multiple(5, 999) - sum_multiple(15, 999)
    
    sum_multiples = simultaneous_sum_multiple_func([3, 5])
    print simultaneous_sum_multiple([3, 5], 999)
    print sum_multiples(999)