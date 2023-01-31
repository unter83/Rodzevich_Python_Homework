from user_interface import WelcomPage, OptionsPage
from imp import ImportBook
from exp import ExportContact

def RunProgram():
    WelcomPage()
    OptionsPage()

def UsersOption(user_choose):
    if user_choose == 1:
        ImportBook()
    elif user_choose == 2:
        ExportContact()