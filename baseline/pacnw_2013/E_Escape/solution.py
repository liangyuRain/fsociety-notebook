import sys
from heapq import heappush, heappop

def is_dest(position):
    return position[0] == 0 \
        or position[1] == 0 \
        or position[0] == h-1 \
        or position[1] == w-1

def solution(ship_dict, graph):
    prioriy_q = []
    seen = set()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'E':
                heappush(prioriy_q, (0, (i, j)))
                seen.add((i,j))
    while prioriy_q:
        cost, position = heappop(prioriy_q)
        if is_dest(position):
            return cost
        x, y = (position[0]-1, position[1])
        if (x, y) not in seen:
            seen.add((x,y))
            heappush(prioriy_q, (cost + ship_dict[graph[x][y]], (x,y)))
        x, y = (position[0], position[1]+1)
        if (x, y) not in seen:
            seen.add((x, y))
            heappush(prioriy_q, (cost + ship_dict[graph[x][y]], (x,y)))
        x, y = (position[0]+1, position[1])
        if (x, y) not in seen:
            seen.add((x, y))
            heappush(prioriy_q, (cost + ship_dict[graph[x][y]], (x,y)))
        x, y = (position[0], position[1]-1)
        if (x, y) not in seen:
            seen.add((x, y))
            heappush(prioriy_q, (cost + ship_dict[graph[x][y]], (x,y)))
    del seen
    del prioriy_q


if __name__ == '__main__':
    f = sys.stdin
    num_tests = int(f.readline())
    for _ in range(num_tests):
        k, w, h = map(int, f.readline().split(" "))
        ship_dict = {}
        for __ in range(k):
            ship_code, ship_num = f.readline().split(" ")
            ship_dict[ship_code] = int(ship_num)

        graph = []
        for __ in range(h):
            graph.append(f.readline().strip())

        print(solution(ship_dict, graph))