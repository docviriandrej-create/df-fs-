A, B, C = map(float, input("Введите A, B, C: ").split())

# Сдвиг значений: A<-B, B<-C, C<-A
A, B, C = B, C, A

print("Новое A:", A)
print("Новое B:", B)
print("Новое C:", C)