print("Программа находит наименьший натуральный делитель числа, отличный от 1")

number = int(input("Введите число для которого требуется найти наименьший делитель: "))

for i in range(2, number + 1):
    if (number == i):
        print(f"Число {number} - простое число")
        break
    if (number % i == 0):
        if (number == i):
            print(f"Число {number} - простое число")
            break
        print(f"Наименьший {i} - делитель для числа {number}")
        break
