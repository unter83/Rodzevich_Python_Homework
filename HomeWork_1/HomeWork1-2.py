print("Программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.\n")
print("Введите значения X, Y, Z в значения 0 или 1 \n")
x, y, z = int(input("X= ")), int(input("Y= ")), int(input("Z= "))
if (x, y, z == 0 or x, y, z == 1):
    x_bool = bool(x)
    y_bool = bool(y)
    z_bool = bool(z)

    if ((not (x_bool and y_bool and z_bool)) == ((not x_bool) or (not y_bool) or (not z_bool))):
        print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для чисел X={x} Y={y} Z={z}")
    else:
        print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не верно для чисел X={x} Y={y} Z={z}")
else:
    print("Используйте только 0 и 1 для ввода значений X, Y, Z")