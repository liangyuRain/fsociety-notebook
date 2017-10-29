import sys

if __name__ == '__main__':
    f = sys.stdin
    for l in f:
        d, s1, s2 = map(int, l.split())
        if l != 0 and s1 != 0 and s2 != 0:
            t1 = float(d) * 3600 / s1 
            t2 = float(d) * 3600 / s2
            delta = round(t1 - t2)
            print "%d:%02d:%02d" % (delta // 3600, (delta // 60) % 60, delta % 60)
        else:
            exit(0)