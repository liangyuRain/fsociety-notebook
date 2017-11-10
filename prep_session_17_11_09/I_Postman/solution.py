import sys

def solution(n, k, houses):
    positive = []
    negative = []
    for house in houses:
        if house[0] >= 0:
            positive.append(house)
        else:
            negative.append([-house[0], house[1]])

    positive = sorted(positive, key=lambda x : x[0])
    negative = sorted(negative, key=lambda x : x[0])
    p_result = helper(n, k, positive)
    n_result = helper(n, k, negative)
    return p_result + n_result

def helper(n, k, houses):
    # assume house sorted according to position
    result = 0

    new_houses = []

    for house in houses:
        result += 2 * house[0] * (house[1] // k)
        if house[1] % k != 0:
            house[1] = house[1] % k
            new_houses.append(house)

    houses = new_houses

    while houses:
        travel_length = houses[-1][0]
        remains = k
        while houses and remains > houses[-1][1]:
            remains -= houses[-1][1]
            houses.pop(-1)
        if houses:
            houses[-1][1] -= remains
        result += 2 * travel_length

    return result


if __name__ == '__main__':
    f = sys.stdin
    # f = open("input/Postman-0000.in")
    n, k = list(map(int, f.readline().split(" ")))
    houses = []
    for _ in range(n):
        x_i, m_i = list(map(int, f.readline().split(" ")))
        houses.append([x_i, m_i])

    print(solution(n, k, houses))
