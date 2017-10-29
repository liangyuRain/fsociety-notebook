import sys


if __name__ == '__main__':
    f = sys.stdin
    for l in f:
        n = int(l)
        if n != 0:
            print(n*(n+1)*(n+2)/6)
        else:
            exit(0)

