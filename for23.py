X = float(input())
N = int(input())
term = X
sum_val = X
for i in range(1, N + 1):
    term *= -X * X / ((2 * i) * (2 * i + 1))
    sum_val += term
print(sum_val)