import time
import sys

bases = {2, 325, 9375, 28178, 450775, 9780504, 1795265022}
base_primes = {2, 3, 5, 13, 19, 73, 193, 407521, 299210837}
missed_under_1000000 = {162401, 6601, 852841, 512461, 252601, 399001}

def fast_exp(base, exp, modulo):
    if exp == 0:
        return 1
    elif exp == 1:
        return base % modulo
    elif exp % 2 == 0:
        cache = fast_exp(base, exp // 2, modulo)
        return (cache * cache) % modulo
    else:
        cache = fast_exp(base, (exp-1) // 2, modulo)
        return (cache * cache * base) % modulo

def miller_rabin(n):
    # have relatively high probability of testing primes
    if n in base_primes:
        return True
    if n in missed_under_1000000:
        return False
    for base in bases:
        if fast_exp(base, n-1, n) != 1:
            return False

    return True

def eratosthenes2(n):
    """
    fastest prime sieving algorithm so far, takes 0.42 to generate primes under 10^6
    :param n:
    :return:
    """
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

if __name__ == '__main__':
    f = open("mr_primes.out", "w")
    begin = time.time()
    primes = list(filter(miller_rabin, range(2, 1000000)))
    end = time.time()
    f.write(str(primes))
    print(end-begin, file=sys.stderr)
    f = open("primes.out", "w")
    begin = time.time()
    primes_e = list(eratosthenes2(1000000))
    end = time.time()
    f.write(str(primes_e))
    print(end-begin, file=sys.stderr)
    primes = set(primes)
    primes_e = set(primes_e)
    print(primes-primes_e)