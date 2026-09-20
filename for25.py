X = float(input())
N = int(input())
term = X
sum_val = X
for i in range(1, N + 1):
    sum_val += term
    term *= -X * i / (i + 1)
print(sum_val)