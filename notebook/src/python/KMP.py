def KMP_table(substr):
    """
    :param substr: the substring need to be matched in a long string
    :return: the KMP table needed in KMP algorithm
    substr[0:table[i]] (INCLUSIVE) represents the longest proper prefix that is a suffix of substr[0:i]
    """
    table = [-1 for _ in range(len(substr))]
    for i in range(1, len(substr)):
        index = table[i - 1]  # substr[0:table[i-1]] represents the longest proper prefix that is a suffix of substr[0:i-1]
        while substr[index + 1] != substr[i]:
            if index == -1:
                index = -2
                break
            index = table[index]  # substr[0:table[index]] is suffix of substr[0:index] which is suffix of substr[0:i-1]
        table[i] = index + 1  # if substr[table[i-1]+1] == substr[i], then table[i] = table[i-1] + 1
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
        index += 1  # substr[0:index] (INCLUSIVE) matches s[i-index:i] where s[i] == c
        if index == len(substr):
            return True
    return False


if __name__ == '__main__':
    substr = 'abc'
    table = KMP_table(substr)
    print(table)
    print(KMP_match('ababababababababababc', substr, table))
    print(KMP_match('ababababababababababa', substr, table))
