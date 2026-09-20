import math
N = int(input())
A = float(input())
B = float(input())
H = (B - A) / N
print(H)
for i in range(N + 1):
    print(1 - math.sin(A + i * H))