N = int(input())
prod = 1.0
for i in range(1, N + 1):
    prod *= (1.0 + i / 10)
print(prod)