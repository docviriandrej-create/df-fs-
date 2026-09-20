N = int(input())
K = int(input())
print(sum(float(i) ** K for i in range(1, N + 1)))