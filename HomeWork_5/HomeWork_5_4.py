print("Программа реализует RLE алгоритм для сжатия и раскрытия строк\n\n")

original_string = input("Введите строку для сжатия: ")
# original_string = original_string  + "1"
print(original_string)
count = 0
li_string = []
flag = False
temp = original_string[0]
for i in original_string:
    # 1. i := a; 2. i := a;  3. i := s;  4. i := s; 5. i := d; 

    if i == temp: # 1. да; 2. да; 3. нет; 4. да
        count += 1  #  1. count := 1; 2. count := 2; 4. count := 1;
    else:
        flag = True
        
    if flag:
        if count == 1: 
            li_string.append(temp)
            count = 0
            emp = i 
        elif count > 1: # 3. да;
            li_string.append(str(count) + temp) # 3. '2a';
            count = 0   # 3. count := 0;
            temp = i   # 3. temp = s;
        
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

print(li_string)