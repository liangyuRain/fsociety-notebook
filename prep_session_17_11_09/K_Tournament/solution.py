import sys
from functools import reduce
from math import gcd

def solution(k, r):
    expectation = 0
    total = 2**k

    numerator = total - k
    denominator = total - 1
    increment = numerator / denominator

    prev_num = total - k
    prev_den = total - 1

    level = 2

    while numerator > 0:
        if increment >= 0.00001:
            expectation += numerator / denominator
        else:
            break
        increment *= reduce(lambda x, y : x*y, range(prev_num-level, prev_num)) / reduce(lambda x, y : x*y, range(prev_den-level, prev_den))
        prev_num -= level
        prev_den -= level
        level *= 2

    return expectation


if __name__ == '__main__':
    f = sys.stdin
    k, r, = list(map(int, f.readline().split(" ")))
    print(solution(k, r))
