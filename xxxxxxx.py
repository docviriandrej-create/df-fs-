N = int(input())
a = N // 100
b = (N // 10) % 10
c = N % 10
print(b * 100 + a * 10 + c)