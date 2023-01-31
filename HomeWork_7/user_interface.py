from imp import ImportBook
from exp import ExportContact, ExportContact2



def WelcomPage():
    print("\n*** Телефонный справочник ***\n")


def OptionsPage():
    print("Выберите действие:")
    print("1 - Показать справочник")
    print("2 - Добавить контакт")
    print("3 - Выйти\n")

    user_choose = (input("Выберите опцию: "))
    

    if user_choose == '1':
        ImportOptions()
    elif user_choose == '2':
        ExportOptions()
    elif user_choose == '3':
        exit()
    else:
        print('Введите одно из указанных значений')
        OptionsPage()

def ExportOptions():
    print("Введите данные:\n")

    s_name = (input("Фамилия: "))
    f_name = (input("Имя: "))
    tel = (input("Телефон: "))
    comment = (input("Коммантарии: "))

    data = (s_name, f_name, tel, comment)
    if ExportContact(data) and ExportContact2(data):
        print('Запись добавлена\n')
    else:
        print('Ошибка записи\n')

    OptionsPage()

def ImportOptions():
    ImportBook()

    OptionsPage()