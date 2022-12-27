print("Программа преобразует десятичное число в двоичное\n")

num = int(input("Введите число: "))

# bin = ""
# div = num 
# rem = 0


# while (div > 0):
#     rem = div % 2
#     div = div // 2
#     print(div, end = " ")
#     if rem == 1:
#         print(1, end = " ")
#         bin = bin + "1"
#     else:
#         print(0, end = " ")
#         bin = bin + "0"

# print()
# print(bin)

bin = ""
div = num 

while (div > 0):
    rem = div % 2
    div = div // 2
    if rem == 1:
        bin = "1" + bin
    else:
        bin = "0" + bin
        
print()
print(f"Число в двоичном виде: {bin}")
