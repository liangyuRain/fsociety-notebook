import sys

def solution(seq):
    intervals = []
    for i in range(1, len(seq)):
        heard = (len(filter(lambda x : i % x == 0, intervals)) % 2) != seq[i]
        if heard:
            intervals.append(i)
    print " ".join(map(str, intervals))
    

if __name__ == '__main__':
    f = sys.stdin
    for l in f:
        seq = map(int, l.strip())
        if len(seq) > 1:
            solution(seq)
