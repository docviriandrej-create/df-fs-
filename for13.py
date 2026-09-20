N = int(input())
sum_val = 0.0
sign = 1
for i in range(1, N + 1):
    sum_val += sign * (1.0 + i / 10)
    sign = -sign
print(sum_val)