def check_symmetry(points):
    x_sums = {}
    for point in points:
        x, y = point[0], point[1]
        if x in x_sums:
            x_sums[x] += y
        else:
            x_sums[x] = y
    for x in x_sums:
        if x_sums[x] != x_sums[-x]:
            return False
    return True
N = int(input("Введите количество точек: "))
points = []
for _ in range(N):
    x, y = map(int, input("Введите координаты точки: ").split())
    points.append((x, y))
if check_symmetry(points):
    print("Существует вертикальная ось симметрии")
else:
    print("Отсутствует вертикальная ось симметрии")
