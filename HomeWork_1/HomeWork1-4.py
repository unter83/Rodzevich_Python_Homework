print("Программу по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). \n")

n = int(input("Введите номер четверти (1, 2, 3, 4): "))

if (n == 1):
    print("Диапазон точек в I четверти (X > 0), (Y > 0)")
elif (n == 2):
    print("Диапазон точек в II четверти (X < 0), (Y > 0)")
elif (n == 3):
    print("Диапазон точек в III четверти (X < 0), (Y < 0)")
elif (n == 4):
    print("Диапазон точек в IV четверти (X > 0), (Y < 0)")
else:
    print("Неправильная четверть")