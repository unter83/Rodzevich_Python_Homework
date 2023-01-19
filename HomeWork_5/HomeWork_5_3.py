
from os import *

def DrawCells(cells_value: list):
    system('cls||clear')
    print("***** Крестики - нолики *****")
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
    
    if (cells_value[cord_in_cell[0]][cord_in_cell[1]] == "X" or cells_value[cord_in_cell[0]][cord_in_cell[1]] == "O"):
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
   
k = 1
cells_value = [[0] * 3 for i in range(3)]

# for i in range(3): 
#    cell.append([0]*3)

# cells_value = {}



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

for i in range(3):
    for j in range (3):
        cells_value[j][i] = str(k)
        k += 1

        # cells_value[k] = cell[j][i]
        # k += 1

DrawCells(cells_value)
cells_count = 0
cord_in_cell = []

while (cells_count < 10): 
    
    if cells_count == 9:
        break
    
    player = int(input("Игрок X - выберите поле: "))
    cord_in_cell = XOInCell(player)

    if CheckCells(cells_value, cord_in_cell, player):
        PutXOInCell(cord_in_cell, cells_value, "X") 
    else:
        continue
    cells_count += 1

    DrawCells(cells_value)


    if cells_count == 9:
        break

    player = int(input("Игрок O - выберите поле: "))
    cord_in_cell = XOInCell(player)

    if CheckCells(cells_value, cord_in_cell, player):
        PutXOInCell(cord_in_cell, cells_value, "O")        
    else:
        continue    
    cells_count += 1
    
    DrawCells(cells_value)



# while (cells_count < 10): 
#     
#     player_x = int(input("Игрок X - выберите поле: "))
#     if (CheckCells(player_x, cells_value) == True):
#         cells_value[player_x] = "X"
#         cells_count += 1
#     else:
#         continue
    
        
#     DrawCells(cells_value)

#     print(                                                                             )
#     if cells_count == 9:
#         break
    
#     player_o = int(input("Игрок O - выберите поле: "))
#     if (CheckCells(player_o, cells_value) == True):
#         cells_value[player_o] = "O"
#         cells_count += 1
#     else:
#         continue
    
#     DrawCells(cells_value)

#     if cells_count == 9:
#         break