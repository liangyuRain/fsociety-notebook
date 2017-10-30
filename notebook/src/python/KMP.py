def KMP_table(substr):
    """
    :param substr: the substring need to be matched in a long string
    :return: the KMP table needed in KMP algorithm
    """
    table = [-1 for _ in range(len(substr))]
    for i in range(1, len(substr)):
        index = table[i - 1]
        while substr[index + 1] != substr[i]:
            if index == -1:
                index = -2
                break
            index = table[index]
        table[i] = index + 1
    return table


def KMP_match(s, substr, table):
    """
    :param s: the long string
    :param substr: the substring need to be matched
    :param table: the KMP table generated in function KMP_table
    :return: True if the substring is found in s, False otherwise
    """
    index = 0
    for c in s:
        while c != substr[index]:
            if index == 0:
                index = -1
                break
            index = table[index - 1] + 1
        index += 1
        if index == len(substr):
            return True
    return False


if __name__ == '__main__':
    substr = 'abc'
    table = KMP_table(substr)
    print(KMP_match('ababababababababababc', substr, table))
    print(KMP_match('ababababababababababa', substr, table))
