A = float(input())
N = int(input())
p = 1.0
sum_val = 0.0
for _ in range(N + 1):
    sum_val += p
    p *= -A
print(sum_val)