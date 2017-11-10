import sys


def solution(s):
    s = [ord(ch) - ord('a') for ch in s]
    opt = [s[i] for i in range(len(s))]
    for j in range(len(s)):
        ptr = s[j] - 1
        for i in reversed(range(j)):
            if s[i] < s[j]:
                opt[j] = min(opt[j], opt[i] + max(0, ptr - s[i]))
                if s[i] == ptr:
                    ptr -= 1
    ptr = 25
    minCost = 26
    for j in reversed(range(len(s))):
        minCost = min(minCost, opt[j] + max(0, ptr - s[j]))
        if s[j] == ptr:
            ptr -= 1
    return minCost


if __name__ == '__main__':
    print(solution(sys.stdin.readline()))
