# ----------CAUTION: this algorithm changes the original array----------
THRESHOLD = 15  # threshold to apply insertion sort, must be odd


def insertionSort(A, l, r):
    """
    :param A: array to be sorted
    :param l: begin of the range inclusive
    :param r: end of the range exclusive
    """
    for i in range(l + 1, r):
        num = A[i]
        j = i
        while j > l and A[j - 1] > num:
            A[j] = A[j - 1]
            j -= 1
        A[j] = num


bucket_size = int(THRESHOLD / 2)


def choosePivot(A, l, r):
    """
    The commented algorithm guarantees the quality of the pivot, and ensures the worst case O(n),
    but runs slow. The uncommented algorithm ensures amortized O(n), but runs much faster.
    :param A: array to be chosen pivot in
    :param l: begin of the range inclusive
    :param r: end of the range exclusive
    :return: the value of the pivot
    """
    # arr = [0] * int((r - l + 1) / THRESHOLD)
    # sl, sr = l, l + THRESHOLD
    # for i in range(len(arr) - 1):
    #     insertionSort(A, sl, sr)
    #     arr[i] = A[sl + bucket_size]
    #     sl += THRESHOLD
    #     sr += THRESHOLD
    # sr = min(r, sr)
    # insertionSort(A, sl, sr)
    # arr[-1] = A[int((sl + sr) / 2)]
    # return select_i_th(arr, int((len(arr) + 1) / 2))
    mid = int((l + r) / 2)
    if A[l] > A[r - 1]:
        A[l], A[r - 1] = A[r - 1], A[l]
    if A[mid] < A[l]:
        A[mid], A[l] = A[l], A[mid]
    elif A[mid] > A[r - 1]:
        A[mid], A[r - 1] = A[r - 1], A[mid]
    return A[mid]


def select_i_th(A, i, l=0, r=None):
    """
    Choose the i_th largest number (i >= 1) in the array in linear time
    :param A: array to be chosen the i_th largest number in
    :param i: i_th
    :param l: begin of the range inclusive
    :param r: end of the range exclusive
    :return: value of the i_th largest number
    """
    r = len(A) if r is None else r
    if r - l <= THRESHOLD:
        insertionSort(A, l, r)
        return A[l + i - 1]
    else:
        pivot = choosePivot(A, l, r)
        a, b, c = l - 1, l, r
        while b < c:
            if A[b] > pivot:
                c -= 1
                A[b], A[c] = A[c], A[b]
            elif A[b] == pivot:
                b += 1
            else:
                a += 1
                A[b], A[a] = A[a], A[b]
                b += 1
        # A[l:a+1] are less than pivot
        # A[a+1:b] are equal to pivot
        # A[b:r] are greater than pivot
        k1, k2 = a - l + 2, b - l
        # the k1-th, (k1+1)-th, ..., k2-th numbers are equal to pivot
        if k1 <= i <= k2:
            return pivot
        elif i < k1:
            return select_i_th(A, i, l, a + 1)
        else:
            return select_i_th(A, i - k2, b, r)


if __name__ == '__main__':
    # A = list(reversed(range(100)))
    # insertionSort(A, 0, 100)
    # print(choosePivot(A, 0, 100))
    # print(A)
    A = list(reversed(range(1000)))
    print(select_i_th(A, 100))
    A = list(reversed(range(10000)))
    print(select_i_th(A, 7000))
    A = list(range(100000))
    print(select_i_th(A, 80000))

    import random
    import time
    size = 10000000
    for THRESHOLD in range(5, 50, 5):
        result1 = result2 = 0
        if THRESHOLD & 1 == 0:
            THRESHOLD += 1
        print(THRESHOLD)
        for _ in range(100):
            A = [random.randint(0, size * 10) for _ in range(size)]
            i = random.randint(1, size)
            B = A.copy()
            start = time.time()
            n1 = select_i_th(A, i)
            end = time.time()
            result1 += end - start
            print(end - start, end='\t')
            start = time.time()
            n2 = sorted(B)[i - 1]
            end = time.time()
            result2 += end - start
            print(end - start)
            if n1 != n2:
                raise 'incorrect'
        print(result1 / 100, result2 / 100, sep='\t')
