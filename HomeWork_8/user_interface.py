from students import ShowStudent, FindStudent, ShowAllStudents
from lessons import ShowLessons
from datetime import datetime
from add_grade import AddGrade

def ShowFirstScreen():
    print('------------------------------------------------------------')
    print('*** Информационная система для преподавателей и учеников ***')
    print('------------------------------------------------------------\n')    

def ShowOptions():
    print("Вы ученик или преподаватель?")
    print("1. Ученик")
    print("2. Преподаватель")
    print("3. Выход\n")

    switch = int(input('Веберите опцию: '))

    if switch == 1:
        print('Вы ученик\n')
        ShowStudentScreen()
    elif switch == 2:
        print('Вы преподаватель\n')
        ShowTeacherScreen()
    elif switch == 3:
        print('Выход\n')
        exit()
    else:
        print('Ошибка ввода\n')
        ShowOptions()
  
def ShowStudentScreen(): 
    print('\nВведите данные ученика\n')
    sec_name = input('Фамилия: ')
    frst_name = input('Имя: ')
    student = FindStudent(frst_name, sec_name)
    if student == 'Not_found':
        print("Ученика не найдено\n")
        CheckChoise('student')
    else:
        print(f'\nЗдравствуйте {student[1]}\n')
        print('Ваши оценки:')
        ShowStudent(student[0])

def CheckChoise(prof):
    if prof == 'student':
        print("Ученика не найдено\n")
        switch = input("Ввести заного? Y/N \n")
        if switch == 'Y' or switch == 'y':
            ShowStudentScreen()
        elif switch == 'N' or switch == 'n':
            ShowOptions()
        else:
            print('Ошибка ввода\n')  
            CheckChoise('student')
    elif prof == 'teacher':
        print("Ученика не найдено\n")
        switch = input("Ввести заного? Y/N \n")
        if switch == 'Y' or switch == 'y':
            ShowTeacherScreen()
        elif switch == 'N' or switch == 'n':
            ShowOptions()
        else:
            print('Ошибка ввода\n')  
            CheckChoise('teacher')
    else:
        ShowOptions()        


def ShowTeacherScreen():
    print("Выберите опцию")
    print("1. Добавить оценку")
    print("2. На уровень вверх")
    print("3. Выйти\n")
    switch = int(input("Выберите опцию:"))
    if switch == 1:
        AddGradeOptions()
    elif switch == 2:
        ShowOptions()
    elif switch == 3:
        print('Выход\n')
        exit()
    else:
        print('Ошибка ввода\n')
        ShowOptions()
    
def AddGradeOptions():
    print('\n Список учеников:')
    student_dict = ShowAllStudents()
    print('\nВведите данные ученика\n')
    student = int(input('Выберите ученика: '))
    print(f'\nЗдравствуйте учитель.\n')
    print(f'Оценки студента {student_dict[student]}:')
    ShowStudent(student)
    print('\n Список уроков:')
    while(True):
        lessons_dict = ShowLessons()
        ls_key = int(input('Выберите урок: '))
        if ls_key not in list(lessons_dict.keys()):
            print('Ошибка ввода урока')
            continue
        break
    while(True):
        grade = int(input('Введите оценку от 1 до 5: '))
        if grade not in range(1,6):
            print('Ошибка ввода оценки')
            continue
        break

    today = input('Сегодня? Y/N: ')
    if today == 'y' or today == 'Y':
        date = datetime.now().strftime('%d.%m.%Y')            
    else:
        date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
    AddGrade(student, ls_key, grade, date)
    print(f' Ученик: {student_dict[student]}. Урок: {lessons_dict[ls_key]}. Поставлена оценка {grade}. Дата: {date}')
