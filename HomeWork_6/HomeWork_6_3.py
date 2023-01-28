print("Программа показывает сумму цифр вещественного числа\n")

num = float(input("Введите число: "))

lst = [int(i) for i in str(num) if i.isdigit()]

print(sum(lst))