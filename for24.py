X = float(input())
N = int(input())
term = 1.0
sum_val = 1.0
for i in range(1, N + 1):
    term *= -X * X / ((2 * i - 1) * (2 * i))
    sum_val += term
print(sum_val)