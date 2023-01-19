
from os import *


def DrawCells(cells_value: dict):
    system('cls||clear')
    print("***** Крестики - нолики *****")
    print()
    print(f" {cells_value[1]} | {cells_value[2]} | {cells_value[3]} ")
    print("---|---|---")
    print(f" {cells_value[4]} | {cells_value[5]} | {cells_value[6]} ")
    print("---|---|---")
    print(f" {cells_value[7]} | {cells_value[8]} | {cells_value[9]} ")
    print()


def CheckCells(player, cells_value) -> bool:
    if (player < 0 or player >= 10):
        DrawCells(cells_value)
        print("Укажите правильный номер клетки от 1 до 9.")
        return False
    if (cells_value[player] == "X" or cells_value[player] == "O"):
        DrawCells(cells_value)
        print("Клетка занята. Укажите ругой номер клетки.")
        return False
    return True

k = 1
cell = [[0] * 3 for i in range(3)]

# for i in range(3): 
#    cell.append([0]*3)

cells_value = {}

for i in range(3):
    for j in range (3):
        cell[j][i] = k
        cells_value[k] = cell[j][i]
        k += 1

# cells_value = \
#     {
#         1: "1",
#         2: "2",
#         3: "3",
#         4: "4",
#         5: "5",
#         6: "6",
#         7: "7",
#         8: "8",
#         9: "9",          
#     }



DrawCells(cells_value)
cells_count = 0

while (cells_count < 10):
    

    
    player_x = int(input("Игрок X - выберите поле: "))
    if (CheckCells(player_x, cells_value) == True):
        cells_value[player_x] = "X"
        cells_count += 1
    else:
        continue
    
    DrawCells(cells_value)

    if cells_count == 9:
        break
    
    player_o = int(input("Игрок O - выберите поле: "))
    if (CheckCells(player_o, cells_value) == True):
        cells_value[player_o] = "O"
        cells_count += 1
    else:
        continue
    
    DrawCells(cells_value)

    if cells_count == 9:
        break