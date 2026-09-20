A, B, C = map(float, input("Введите координаты A, B, C: ").split())

AC = abs(C - A)
BC = abs(C - B)
sum_lengths = AC + BC

print("Длина AC:", AC)
print("Длина BC:", BC)
print("Сумма длин:", sum_lengths)