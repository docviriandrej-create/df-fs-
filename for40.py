A = int(input())
B = int(input())
for i in range(A, B + 1):
    for _ in range(i - A + 1):
        print(i)