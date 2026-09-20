x1, y1 = map(float, input("Введите координаты первой вершины (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2 y2): ").split())

a = abs(x2 - x1)
b = abs(y2 - y1)

P = 2 * (a + b)
S = a * b

print("Периметр:", P)
print("Площадь:", S)