import math
print("Программа выводит число ПИ до определённого пользователем знака.\n")

k = int(input("?"))
pi=0
for i in range(0,k):
    pi = pi + ((-1)**i * math.factorial(6 * i) * (13591409 + 545140134 * i)) / (math.factorial(3 * i) * pow(math.factorial(i), 3) * pow(640320, 3 * i + 3/2))

pi = pow(12*pi, -1)
print("%.3f" % pi)