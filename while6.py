N = int(input())
prod = 1.0
while N > 0:
    prod *= N
    N -= 2
print(prod)