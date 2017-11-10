import sys
from functools import reduce
from math import gcd

def solution(k, r):
    expectation = 0
    total = 1 << k
    below = total - r
    probability = 1.0
    choices = total - 1

    for i in range(k):
        for j in range((1<<i) - 1, (1<<(i+1)) - 1):
            probability *= (below - j) / (choices - j)
        if probability == 0.0:
            break
        else:
            expectation += probability

    return expectation


if __name__ == '__main__':

    k, r, = list(map(int, input().split(" ")))
    print("%.5lf" % solution(k, r))
