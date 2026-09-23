N = int(input())
K = int(input())
quotient = 0
while N >= K:
    N -= K
    quotient += 1
print(quotient, N)