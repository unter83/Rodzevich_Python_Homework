print("Программа считает сумму чётных чисел, расположенных между числами 1 и N (включительно)\n")

num = int(input("Введите число N: "))
if num <= 0:
    print("N должно быть больше 0")
sum = 0
for i in range(0, num + 1, 2):
    print(i, end=" ")
    sum += i

print(f"\nСумма чисел {sum}")