

if __name__ == '__main__':
    a1, b1, c1 = sorted(map(int, input().split(" ")))
    a2, b2, c2 = sorted(map(int, input().split(" ")))
    if a1*a1 + b1*b1==c1*c1 and a1==a2 and b1==b2 and c1==c2:
        print("YES")
    else:
        print("NO")