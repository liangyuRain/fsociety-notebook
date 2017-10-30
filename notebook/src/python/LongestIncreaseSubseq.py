import bisect


def lengthOfLIS(nums):
    """
    :param nums: sequence list of numbers
    :return: the length of the longest increasing subsequence
             (the adjacent elements in subsequence may not be adjacent in original sequence)
    """
    seq = []  # Notice: this is not the resulting subsequence
    for n in nums:
        index = bisect.bisect_left(seq, n)
        if index == len(seq):
            seq.append(n)
        else:
            seq[index] = n
    return len(seq)


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS(range(1000)))
    print(lengthOfLIS(reversed(range(1000))))
