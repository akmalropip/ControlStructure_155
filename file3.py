n = int(input("Masukkan n: "))

a = 1
b = 15

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b