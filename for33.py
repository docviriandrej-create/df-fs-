N = int(input())
f1, f2 = 1, 1
print(f1)
if N > 1:
    print(f2)
for _ in range(3, N + 1):
    f1, f2 = f2, f1 + f2
    print(f2)