N = int(input())
while N % 3 == 0:
    N //= 3
print(N == 1)