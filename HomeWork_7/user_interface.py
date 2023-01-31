from imp import ImportBook
from exp import ExportContact



def WelcomPage():
    print("\n*** Телефонный справочник ***\n")


def OptionsPage():
    print("Выберите действие:")
    print("1 - Показать справочник")
    print("2 - Добавить контакт")
    print("3 - Выйти\n")

    user_choose = (int(input("Выберите опцию: ")))

    if user_choose == 1:
        ExportOptions()
    elif user_choose == 2:
        ExportOptions()
    elif user_choose == 3:
        exit()

def ExportOptions():
    print("Введите данные:\n")

    s_name = (input("Фамилия: "))
    f_name = (input("Имя: "))
    tel = (input("Телефон: "))
    comment = (input("Коммантарии: "))

    ExportContact(s_name, f_name, tel, comment)
    OptionsPage()