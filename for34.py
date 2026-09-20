N = int(input())
a1, a2 = 1.0, 2.0
print(a1)
if N > 1:
    print(a2)
for _ in range(3, N + 1):
    a1, a2 = a2, (a1 + 2 * a2) / 3
    print(a2)