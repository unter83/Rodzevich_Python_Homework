
import random

print("\n*** Игра в конфеты ***\n")
print("На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.\nПервый ход делает человек. За один ход можно забрать не более чем 28 конфет.\n")

# def ToDigit()

def Player1_Takes_Candy(candy_pool) -> int:
    player1_takes_candy = False    
    while (not player1_takes_candy):
        candy_taken = input("Возьмите от 1 до 28 конфет: ")
        if candy_taken.isdigit():
            candy_taken = int(candy_taken)
            if (candy_taken > 0 and candy_taken <= 28):
                if candy_pool >= candy_taken:
                    print(f"Игрок берёт {candy_taken} конфет\n")
                    player1_takes_candy = True
                else:
                    candy_taken = candy_pool
                    print(f"Игрок берёт {candy_taken} конфет\n")
                    player1_takes_candy = True  
            else:
                print("Вы можете взять от 1 до 28 конфет")
        else:
            print("Введите число")
    return candy_taken

def Bot_Takes_Candy(candy_pool) -> int:
    candy_taken = random.randint(1,29)

    if candy_pool >= candy_taken:
        print(f"Компьютер берёт {candy_taken} конфет\n")
    else:
        candy_taken = candy_pool
        print(f"Компьютер берёт {candy_taken} конфет\n")

    return candy_taken

def ShowCandyPool(candy_pool):
    print(f"На столе лежит {candy_pool} конфет \n")
   
def IsVictory(candy_pool):
    if candy_pool <= 0:
        return True
    else:
        return False

candy_pool = 120
player1_candy = 0
player_bot_candy = 0
candy_taken = 0
roll = 0

while (candy_pool > 0):
    roll += 1
    print(f"-Раунд {roll}-\n")
    candy_taken = Player1_Takes_Candy(candy_pool)
    candy_pool -= candy_taken
    player1_candy += candy_taken

    if IsVictory(candy_pool):
        print(f"Победил игрок\n")
        break

    candy_taken = Bot_Takes_Candy(candy_pool)
    candy_pool -= candy_taken
    player_bot_candy += candy_taken
    ShowCandyPool(candy_pool)

    if IsVictory(candy_pool):
        print(f"Победил компьютер\n")
        break


    

