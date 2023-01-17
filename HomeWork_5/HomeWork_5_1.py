
import random

print("Игра в конфеты\n")
print("На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.\nПервый ход делает человек. За один ход можно забрать не более чем 28 конфет.\n")

# def Player_Take_Candy() -> int:
#     candy_taken = int(input("Возьмите от 1 до 28 конфет: "))
#     if (candy_taken > 0 and candy_taken <= 28):
#         return candy_taken
#     else:
#         Player_Take_Candy()

def Player1_Takes_Candy() -> int:
    player1_takes_candy = False    
    while (not player1_takes_candy):
        candy_taken = int(input("Возьмите от 1 до 28 конфет: "))
        
        if (candy_taken > 0 and candy_taken <= 28):
            player1_takes_candy = True
        else:
            print("Вы можете взять от 1 до 28 конфет")

    return candy_taken

def Player_Bot_Takes_Candy() -> int:
    candy_taken = random.randint(1,29)
    print(f"Компьютер берёт {candy_taken} конфет")
    return candy_taken

candy_pool = 120
player1_candy = 0
player_bot_candy = 0
candy_taken = 0

print(f"candy - {candy_pool}")
print(f"player1_candy - {player1_candy}")
print()

while (candy_pool > 0):

    candy_taken = Player1_Takes_Candy()
    candy_pool -= candy_taken
    player1_candy += candy_taken
    print(f"candy - {candy_pool}")
    print(f"player1_candy - {player1_candy}")
    print()

    candy_taken = Player_Bot_Takes_Candy()
    candy_pool -= candy_taken
    player_bot_candy += candy_taken
    print(f"candy - {candy_pool}")
    print(f"player_bot_candy - {player_bot_candy}")
    print()
    

