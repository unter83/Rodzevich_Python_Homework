import math

print("Программа, принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. \n")

print("Ввежите координаты первой точки \n")

a_x, a_y = int(input("X1 = ")), int(input("Y1 = "))

print("Ввежите координаты второй точки  \n")

b_x, b_y = int(input("X2 = ")), int(input("Y2 = "))

r = float(math.sqrt(((a_x - b_x)**2) + ((a_y - b_y)**2)))

print(f"Расстояние между дочками A({a_x}, {a_y}) и B({b_x}, {b_y}) равно {round(r, 2)}")


