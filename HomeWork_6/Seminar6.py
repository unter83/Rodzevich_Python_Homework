def EnterTheString() -> str:
    is_example_wright = False
    while (is_example_wright == False):
        example = input("Введите выражение для вычисления: ")
        for i in example:
            if str(i).isdigit() or (i == ' ' or i == '+' or i == '-' or i == '*' or i == '/'):
                is_example_wright = True
            else:
                is_example_wright == False
                print("Убедитесь что в выражении только допустимые символы.")
                example = input("Введите выражение для вычисления: ")        
                break       
    return example

def CalculateElements(example) -> list:
    result_list = []    
    for elem in example:
        if str(elem).isdigit() or (elem[0] == "-" and str(elem).isdigit()):
            result_list.append(int(elem))
        else:                
            i, j = 0, 0
            result = 1  
            while i < len(elem):           
                  
                if (elem[i] == "*" and j == 0) or (elem[i] == "/" and j == 0):
                    result = int(elem[j:i])                
                    j = i
                    i += 1
                    continue

                if (elem[i] == "*" or elem[i] == "/") and elem[j] == "*":
                    result = result * int(elem[j + 1:i])
                    j = i
                    i += 1
                    continue
                elif (elem[i] == "*" or elem[i] == "/") and elem[j] == "/":
                    result = result / int(elem[j + 1:i])
                    j = i
                    i += 1
                    continue

                if i == len(elem) - 1 and elem[j] == "*":
                    result = result * int(elem[j + 1:i + 1])
                    j = i
                    i += 1
                    continue
                elif i == len(elem) - 1 and elem[j] == "/":
                    result = result / int(elem[j + 1:i + 1])
                    j = i
                    i += 1
                    continue
                i += 1

            result_list.append(result)
    return result_list
    

def Main():
    example = EnterTheString()
    example = example.replace(" ","")
    print(example)
    example = example.replace("+"," +")
    print(example)
    example = example.replace("-"," -")
    print(example)
    example = example.split()
    print(example)

    result_list = CalculateElements(example)
    print(result_list)

    overall = 0    
    for i in result_list:
        overall = overall + i

    print(overall)


    
Main()