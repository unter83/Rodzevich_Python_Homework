print("Программа выдаёт список чисел Фибоначчи, в том числе для отрицательных индексов (-N, N).\n")

k = int(input("Введите диапазон чисел Фибоначчи (N): "))
fib = [0, 1]
i = 2
for i in range(2, k+1):
    fib.append(fib[i-1]+fib[i-2])
fib2 = []
for i in range(1, k+1):
    fib2.append(pow(-1, i+1) * fib[i])
fib2 = list(reversed(fib2))
fib3 = fib2 + fib
print("Негафибоначчи: ")
print(fib3)
