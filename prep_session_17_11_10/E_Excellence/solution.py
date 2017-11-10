import sys
from math import inf

def solution(n, ratings):
    min_rating = inf
    ratings = sorted(ratings)
    for i in range(n // 2):
        temp = ratings[i] + ratings[-i-1]
        if temp < min_rating:
            min_rating = temp

    return min_rating

if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    ratings = []
    for _ in range(n):
        ratings.append(int(f.readline()))
    print(solution(n, ratings))
