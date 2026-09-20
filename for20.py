N = int(input())
p = 1.0
sum_val = 0.0
for i in range(1, N + 1):
    p *= i
    sum_val += p
print(sum_val)