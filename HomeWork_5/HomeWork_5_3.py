
from os import *

def DrawCells(cells_value: list):
    system('cls||clear')
    print("***** Крестики - нолики *****")
    print("Игрок 1 ставит за крестики")
    print("Игрок 2 ставит за нолики")
    print()
    print(f" {cells_value[0][0]} | {cells_value[1][0]} | {cells_value[2][0]} ")
    print("---|---|---")
    print(f" {cells_value[0][1]} | {cells_value[1][1]} | {cells_value[2][1]} ")
    print("---|---|---")
    print(f" {cells_value[0][2]} | {cells_value[1][2]} | {cells_value[2][2]} ")
    print()


def CheckCells(cells_value, cord_in_cell, player) -> bool:
    if (player < 0 or player >= 10):
        DrawCells(cells_value)
        print("Укажите правильный номер клетки от 1 до 9.")
        return False
    
    if (cells_value[cord_in_cell[0]][cord_in_cell[1]] == "X" or 
        cells_value[cord_in_cell[0]][cord_in_cell[1]] == "O"):
        DrawCells(cells_value)
        print("Клетка занята. Укажите ругой номер клетки.")
        return False
    return True

def XOInCell(player) -> list:
    if player == 1:
        return [0,0]
    elif player == 2:
        return [1,0]
    elif player == 3:
        return [2,0]
    elif player == 4:
        return [0,1]
    elif player == 5:
        return [1,1]
    elif player == 6:
        return [2,1]
    elif player == 7:
        return [0,2]
    elif player == 8:
        return [1,2]
    elif player == 9:
        return [2,2]

def PutXOInCell(cord_in_cell, cells_value, mark):
    cells_value[cord_in_cell[0]][cord_in_cell[1]] = mark

def CheckHVLines(cord_in_cell, cells_value, mark) -> bool:
    victory_count = 0
    for i in range(3):
        if cells_value[cord_in_cell[0]][i] == mark:
            victory_count += 1
            # print("вертикаль да" + f" Значение {cells_value[cord_in_cell[0]][i]} Вик {victory_count}")
        else:
            # print("вертикаль нет" + f" Значение {cells_value[cord_in_cell[0]][i]} Вик {victory_count}")
            victory_count = 0
            break
        if victory_count == 3:
            # ("вертикаль победа" + f"{victory_count}")
            return True
    victory_count = 0

    for i in range(3):
        if cells_value[i][cord_in_cell[1]] == mark:
            victory_count += 1
            # print("горизонталь да" + f" Значение {cells_value[i][cord_in_cell[1]]} Вик {victory_count}")
        else:
            # print("горизонталь нет" + f" Значение {cells_value[i][cord_in_cell[1]]} Вик {victory_count}")
            victory_count = 0
            break
        if victory_count == 3:
            # print("горизонталь победа" + f"{victory_count}")
            return True
        victory_count = 0

def IsVictory(player, cord_in_cell, cells_value, mark):
    victory_count = 0
    if player % 2 == 0:
        if CheckHVLines(cord_in_cell, cells_value, mark):
            return True

    else:
        if CheckHVLines(cord_in_cell, cells_value, mark):
            return True
        
        for i in range(3):
            if cells_value[i][i] == mark:
                victory_count += 1
                # print("гл. диагональ да" + f" Значение {cells_value[i][i]} Вик {victory_count}")
            else:
                # print("гл. диагональ нет" + f" Значение {cells_value[i][i]} Вик {victory_count}")
                victory_count = 0
                break
            if victory_count == 3:
                # print("гл. диагональ победа")
                return True
        victory_count = 0

        for i in range(3):
            if cells_value[2 - i][i] == mark:
                # print("диагональ да" + f" Значение {cells_value[2 - i][i]} Вик {victory_count}")
                victory_count += 1
            else:
                # print("диагональ нет" + f" Значение {cells_value[2 - i][i]} Вик {victory_count}")
                victory_count = 0
                break
            if victory_count == 3:
                # print("диагональ победа")
                return True
        victory_count = 0
        
    return False


k = 1
cells_value = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range (3):
        cells_value[j][i] = str(k)
        k += 1

DrawCells(cells_value)
cells_count = 0
cord_in_cell = []

while (cells_count < 10): 
    
    if cells_count == 9:
        print("Ничья")
        break
    
    player = int(input("Игрок 1: Выберите поле чтобы поставить крестик: "))
    cord_in_cell = XOInCell(player)

    if CheckCells(cells_value, cord_in_cell, player):
        PutXOInCell(cord_in_cell, cells_value, "X") 
    else:
        continue
    
    cells_count += 1
    DrawCells(cells_value)

    if IsVictory(player, cord_in_cell, cells_value, "X"):
        print("Игрок 1 лобедил: ")
        break
    
    if cells_count == 9:
        print("Ничья")
        break

    player = int(input("Игрок 2: Выберите поле чтобы поставить нолик: "))
    cord_in_cell = XOInCell(player)

    if CheckCells(cells_value, cord_in_cell, player):
        PutXOInCell(cord_in_cell, cells_value, "O")        
    else:
        continue    

    cells_count += 1
    DrawCells(cells_value)   

    if IsVictory(player, cord_in_cell, cells_value, "O"):
        print("Игрок 2 лобедил: ")
        break

