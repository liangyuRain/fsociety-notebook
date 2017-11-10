import sys

class Classy(object):

    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __cmp__(self, other):
        for i in range(min(len(self.classes), len(other.classes))):
            if self.classes[i] < other.classes[i]:
                return -1
            elif self.classes[i] > other.classes[i]:
                return 1

        if self.name < other.name:
            return 1
        elif self.name == other.name:
            return 0
        else:
            return -1

    def __le__(self, other):
        return self.__cmp__(other) < 0

    def __ge__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) >= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __repr__(self):
        return self.name + ": " + str(self.classes)


def solution(classies):
    print(classies)
    classies = sorted(classies, reverse=True)
    for c in classies:
        print(c.name)

if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())

    classies = []

    def map_class(class_str):
        if class_str == 'lower':
            return 0
        elif class_str == 'middle':
            return 1
        else:
            return 2

    for _ in range(n):
        name, classes = f.readline().split(":")
        classes = classes.split(" ")
        classes.pop(0)
        classes.pop(-1)
        classes = list(reversed(list(map(map_class, classes))))
        classies.append(Classy(name, classes))

    solution(classies)


