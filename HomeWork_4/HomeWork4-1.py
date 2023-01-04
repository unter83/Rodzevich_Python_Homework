import math
print("Программа выводит число ПИ до определённого пользователем знака. Точность не более 14 знаков\n")

n = (input("Введите число знаков после запятой (не более 14): "))
if int(n) < 15:
    pi = 0.0
    for i in range(0, 18):
        pi = pi + ((-1)**i * math.factorial(6 * i) * (13591409 + 545140134 * i)) / (math.factorial(3 * i) * pow(math.factorial(i), 3) * pow(640320, 3 * i + 3/2))
    pi = pow(12*pi, -1)
    print(f"%.{n}f" % pi)
else:
    print("Значение должно быть не более 14")
