print("Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.")

number = int(input("Введите число N: "))

list = []
prod = 1

for i in range(1, number + 1):
    prod *= i
    list.append(prod)

print(list)