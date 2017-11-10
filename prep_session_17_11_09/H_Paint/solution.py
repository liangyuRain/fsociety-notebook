import bisect
import sys


def solution(n, ps):
    ps.sort(key=lambda e: (e[1], e[0]))
    starts = [e[0] for e in ps]
    ends = [e[1] for e in ps]
    opt = [n for _ in ps]
    for i in range(len(opt)):
        j = bisect.bisect_left(ends, starts[i], hi=i) - 1
        maxStart = 0
        while j >= 0 and ends[j] >= maxStart and starts[i] - ends[j] - 1 < opt[i]:
            maxStart = max(maxStart, starts[j])
            opt[i] = min(opt[i], opt[j] + starts[i] - ends[j] - 1)
            j -= 1
        opt[i] = min(opt[i], starts[i] - 1)
    result = n
    for i in range(len(opt)):
        result = min(result, opt[i] + n - ends[i])
    return result


n, k = sys.stdin.split()
n, k = int(n), int(k)
ps = [None for _ in range(k)]
i = 0
for l in sys.stdin:
    a, b = l.split()
    a, b = int(a), int(b)
    ps[i] = (a, b)
    i += 1
print(solution(n, ps))
