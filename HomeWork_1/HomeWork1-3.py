print("Программа принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится) \n")

print("Введите координаты точки:")
x, y = int(input("X = ")), int(input("Y = "))

if (x == 0 and y == 0):
    print("Точка находится в точке (0, 0)")
elif (x == 0):
    print("Точка находится на оси абцисс")
elif (y == 0):
    print("Точка находится на оси ординат")
else:
    if (x > 0 and y > 0):
        print("Точка находится в I четверти")
    elif (x < 0 and y > 0):
        print("Точка находится в II четверти")
    elif (x < 0 and y < 0):
        print("Точка находится в III четверти")
    elif (x > 0 and y < 0):
        print("Точка находится в III четверти")