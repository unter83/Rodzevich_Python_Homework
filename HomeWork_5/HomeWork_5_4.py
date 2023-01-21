

def ZipString(original_string) -> str:
    flag = 0
    count = 0
    new_string = ""
    temp = original_string[0]
    for i in original_string:
        flag += 1
        if i == temp:
            count += 1
        else:
            if count == 1:
                new_string = new_string + temp
                count = 1
                temp = i
            elif count > 1:
                new_string = new_string + str(count) + temp
                count = 1
                temp = i
        if flag == len(original_string):
            if count == 1:
                new_string = new_string + temp
                count = 1
                temp = i
            elif count > 1:
                new_string = new_string + str(count) + temp
                count = 1
                temp = i
    return new_string

def UnzipString(zip_string) -> str:
    unzip_string = ""
    digit_num = 0
    digit_string = ""
    for i in zip_string:
        if str(i).isdigit():
            digit_num += 1    
            digit_string += i
        else:
            if digit_num > 0:
                for k in range(int(digit_string)):
                    unzip_string += i
            else:
                unzip_string += i
            digit_string = ""
            digit_num = 0

    return unzip_string

def main():
    print("Программа реализует RLE алгоритм для сжатия и раскрытия строк\n\n")

    original_string = input("Введите строку для сжатия: ")
    print()
    print(f"Исходная строка стока - {original_string}\n")
    new_string = ZipString(original_string) 
    print(f"Архивированная стока - {new_string}\n")
    unzip_string = UnzipString(new_string)   
    print(f"Разархивированная стока - {unzip_string}\n")

main()
# count = 0
# li_string = []
# letters_counter = 1
# while count < len(original_string) - 1:
#     if original_string[count] == original_string[count + 1]:
#         letters_counter += 1
#         count += 1
#         if letters_counter == 1:
#             li_string.append(original_string[count])
#             letters_counter = 1
#         else:
#             li_string.append(str(letters_counter) + original_string[count])
#             letters_counter = 1
#     else:
#         if letters_counter == 1:
#             li_string.append(original_string[count])
#             letters_counter = 1
#         else:
#             li_string.append(str(letters_counter) + original_string[count])
#             letters_counter = 1
#     count += 1

