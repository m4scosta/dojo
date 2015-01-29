# coding: utf8

import math


def eratosthenes_sieve(n):
    primes = range(2, int(math.sqrt(n)) + 1) + [n]

    i = 0
    while i < len(primes):
        primes = [primes[i]] + filter(lambda x: x % primes[i] != 0, primes)
        i += 1

    return primes


def is_prime(n):
    return n in eratosthenes_sieve(n)


def prime_factors(n):

    if is_prime(n):
        return {n: 1}

    factors = {}

    i = 2
    while n != 1:
        if n % i == 0 and is_prime(i):
            factors[i] = factors.get(i, 0) + 1
            n = n / i
        else:
            i += 1

    return factors
