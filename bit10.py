import math
def check_symmetry(points):
    points = set([tuple(point) for point in points])
    min_x, max_x = math.inf, -math.inf
    for x, i in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
    qx = (min_x + max_x) / 2
    for x, y in points:
        if x < qx and (qx + (qx - x), y) not in points:
            return 0
        if x > qx and (qx - (x - qx), y) not in points:
            return 0
    return 1

if __name__ == "__main__":
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append(list([x, y]))
    print(check_symmetry(points))