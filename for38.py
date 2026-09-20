N = int(input())
print(sum(float(i) ** (N - i + 1) for i in range(1, N + 1)))