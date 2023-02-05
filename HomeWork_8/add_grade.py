from lessons import GetLessons
from students import GetSudents, FindStudent

def AddGrade(std_key, ls_key, grade, date):
    student_dict = GetSudents()
    lessons_dict = GetLessons()
    
    path = 'HomeWork_8/Students/' + str(std_key) + '.txt'
    with open(path,'a', encoding='utf8') as file:
        file.writelines(f'{lessons_dict[ls_key]} | Оценка: {grade} | Дата: {date}\n')