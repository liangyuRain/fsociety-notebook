def log2floor(x: int) -> int:
    return x.bit_length() - 1


class RangeMax:

    """
    Construction: O(n*log(n))
    Query: O(1)
    self.memo[j][i] stores the maximum value in the range [i, i+2^j)

    To compute self.memo[j][i], we have
        self.memo[j][i] = max(self.memo[j - 1][i], self.memo[j - 1][i + 2 ** (j - 1)])
    i.e., max(arr[i : i+2^j]) = max(max(arr[i : i+2^(j-1)]), max(arr[i+2^(j-1) : i+2^j))

    To query max(arr[l : r]), we find the largest j such that 2^j <= r - l,
    and return max(self.memo[j][l], self.memo[j][r - 2^j])
    i.e., max(arr[l : r]) = max(max(arr[l : l+2^j]), max(arr[r-2^j : r))
    """
    def __init__(self, arr: list):
        assert len(arr) > 1
        self.memo = []
        self.memo.append([x for x in arr])
        for j in range(1, log2floor(len(arr)) + 1):
            self.memo.append(
                [max(self.memo[j - 1][i], self.memo[j - 1][i + 2 ** (j - 1)])
                 for i in range(len(arr) - 2 ** j + 1)]
            )
    

    def query(self, l: int, r: int) -> int:
        assert l < r
        if r - l == 1:
            return self.memo[0][l]
        j = log2floor(r - l)
        return max(self.memo[j][l], self.memo[j][r - 2 ** j])


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(100)]
    rangeMax = RangeMax(arr)
    for _ in range(1000):
        l = random.randint(0, len(arr) - 1)
        r = random.randint(l + 1, len(arr))
        assert rangeMax.query(l, r) == max(arr[l : r])
