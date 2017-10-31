def isPowerOfTwo(n):
    return (n & (n - 1)) == 0 and n != 0


if __name__ == '__main__':
    print(isPowerOfTwo(1024))
    print(isPowerOfTwo(1025))
