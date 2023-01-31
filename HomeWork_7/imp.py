def ImportBook():
    print("Импорт контактов\n")
    path = 'HomeWork_7/contacts.txt'
    with open(path, 'r') as file:
        text = file.read()

    print(text + '\n')
    
    




