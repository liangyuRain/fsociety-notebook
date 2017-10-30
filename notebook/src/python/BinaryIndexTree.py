class FenwickTree:

    def __init__(self, arg, copy=False):
        """
        :param arg: if arg is an int, construct a all zero fenwick tree;
                    Otherwise, try to build a list on with list(arg) and construct fenwick tree based on it
        :param copy: whether make a copy of the array
        """
        if isinstance(arg, int):
            self.fenArr = [0] * (arg + 1)
            self.arr = [0] * arg
        else:
            size = len(arg)
            self.fenArr = [0] * (size + 1)
            if copy or not isinstance(arg, list):
                self.arr = list(arg)
            else:
                self.arr = arg
            for i in range(size):
                index = i + 1
                while index < size + 1:
                    self.fenArr[index] += self.arr[i]
                    index += index & (-index)
        self.threshold = len(self.arr).bit_length() + 1  # slightly over estimate the steps needed to compute a sum

    def update(self, index, value):
        self[index] = value
        return value

    def getSum(self, end):
        """
        :param end: end of the range inclusive
        :return: sum of arr[0...end] inclusive
        """
        if end <= self.threshold:  # if the range is small, directly use built-in sum
            return sum(self.arr[:end + 1])
        else:
            end += 1
            result = 0
            while end > 0:
                result += self.fenArr[end]
                end -= end & (-end)
            return result

    def rangeSum(self, begin, end):
        """
        :param begin: begin of the range inclusive
        :param end: end of the range inclusive
        :return: sum of arr[begin...end] inclusive
        """
        if end - begin <= 2 * self.threshold:
            return sum(self.arr[begin:end + 1])
        else:
            return self.getSum(end) - self.getSum(begin - 1)

    def clear(self):
        """
        Reset all elements in the tree to zero
        """
        for i in range(len(self.arr)):
            self.arr[i] = 0
            self.fenArr[i] = 0
        self.fenArr[-1] = 0

    def __getitem__(self, index):
        """
        :param index: index of the element
        :return: the number at specific index
        """
        return self.arr[index]

    def __setitem__(self, index, value):
        """
        :param index: the index of the number need to be updated
        :param value: the updated value
        :return: the updated value
        """
        diff = value - self.arr[index]
        self.arr[index] = value
        index += 1
        while index < len(self.fenArr):
            self.fenArr[index] += diff
            index += index & (-index)
        return value

    def __len__(self):
        """
        :return: size of the tree
        """
        return len(self.arr)


if __name__ == '__main__':
    tree = FenwickTree(range(100000))
    # tree = FenwickTree(100000)
    print(tree.threshold)
    print(tree.rangeSum(10, 5000))
    n = tree[500] = 500 + 1000
    print(n)
    print(tree.rangeSum(10, 5000))
    tree[5000] += 1000
    print(tree.rangeSum(10, 5000))
    tree.clear()
    print(tree.getSum(len(tree) - 1))
