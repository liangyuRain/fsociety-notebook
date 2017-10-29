import sys

possible = [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0), (-1, 1, 1), (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1)]


def blockIdx(x, k):
    return x / k


def cmpPoints(p1, p2, k):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2 < k


def cmpBlocks(b1, b2, k):
    count = 0
    for p1 in b1:
        for p2 in b2:
            if p1 != p2 and cmpPoints(p1, p2, k):
#                 print '{0}----{1}'.format(p1, p2)
                count += 1
    return count


def insideBlocks(ps, k):
    count = 0
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            if cmpPoints(ps[i], ps[j], k):
#                 print '{0}----{1}'.format(ps[i], ps[j])
                count += 1
    return count


def solution(coords, k):
    blocks = {}
    for p in coords:
        x, y, z = p
        bx, by, bz = blockIdx(x, k), blockIdx(y, k), blockIdx(z, k)
        if (bx, by, bz) not in blocks:
            blocks[bx, by, bz] = [p]
        else:
            blocks[bx, by, bz].append(p)
    k = k ** 2
#     print blocks
    count = 0
    for ps in blocks.itervalues():
        count += insideBlocks(ps, k)
    for b in blocks:
        x, y, z = b
        for diff in possible:
            dx, dy, dz = diff
            bx, by, bz = x + dx, y + dy, z + dz
            if (bx, by, bz) in blocks:
                count += cmpBlocks(blocks[x, y, z], blocks[bx, by, bz], k)
    return count
    

if __name__ == '__main__':
    f = sys.stdin
    n = k = 0
    coords = []
    for l in f:
        if n == 0:
            n, k = l.split()
            n = int(n)
            k = int(k)
            coords = []
        else:
            x, y, z = l.split()
            coords.append((int(x), int(y), int(z)))
            n -= 1
            if n == 0:
                print solution(coords, k)

