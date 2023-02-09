from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import random

max_candy = 28
max_candy_pool = 120

P0 = 0
P1 = 1
P2 = 2
P3 = 3
P4 = 4

candy_pool = max_candy_pool 
player1_candy = 0
player_bot_candy = 0
candy_taken = 0
roll = 0
rounds_left = int(max_candy_pool / max_candy)


def Player1_Takes_Candy(update, context):
    candy_taken = update.message.text  
    global candy_pool, rounds_left
    # player1_takes_candy = False  
    if candy_taken.isdigit():
        candy_taken = int(candy_taken)
        if (candy_taken > 0 and candy_taken <= max_candy):
            if candy_pool >= candy_taken:
                context.bot.send_message(update.effective_chat.id, f"Игрок берёт {candy_taken} конфет")
                candy_pool = candy_pool - candy_taken
                context.bot.send_message(update.effective_chat.id, f"На столе осталось {candy_pool} конфет")
                # print(f"Игрок берёт {candy_taken} конфет\n")
                # player1_takes_candy = True
                if candy_pool <= 0:
                    context.bot.send_message(update.effective_chat.id, f"Победил игрок")
                    return P4
                Bot_Takes_Candy(update, context)                
                return P1
            else:
                candy_taken = candy_pool                
                candy_pool = 0
                context.bot.send_message(update.effective_chat.id, f"Игрок берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
                if candy_pool <= 0:
                    context.bot.send_message(update.effective_chat.id, f"Победил игрок")
                    return P4 
                Bot_Takes_Candy(update, context) 
                # print(f"Игрок берёт {candy_taken} конфет\n")
                # player1_takes_candy = True
                return P1  
        else:
            context.bot.send_message(update.effective_chat.id, f"Вы можете взять от 1 до {max_candy} конфет")
            # print(f"Вы можете взять от 1 до {max_candy} конфет")
            return P2
    else:
        context.bot.send_message(update.effective_chat.id, "Введите число")
        # print("Введите число")
        return P3

   

def Bot_Takes_Candy(update, context):
    global candy_pool, rounds_left
    if (candy_pool > 1 + max_candy * rounds_left):
        if rounds_left > 0:
            candy_taken = candy_pool - (1 + max_candy * rounds_left)
            candy_pool -= candy_taken
        else:
            candy_taken = candy_pool 
            candy_pool -= candy_taken
        context.bot.send_message(update.effective_chat.id, f"Компьютер берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
        rounds_left -= 1
        if candy_pool <= 0:
            context.bot.send_message(update.effective_chat.id, f"Победил компьютер")
            return P4      
    
    else:
        if rounds_left > 1:
            candy_taken = candy_pool - (1 + max_candy * (rounds_left - 1))
            candy_pool -= candy_taken
        else:
            candy_taken = candy_pool
            candy_pool -= candy_taken
        context.bot.send_message(update.effective_chat.id, f"Компьютер берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
        rounds_left -= 1
        if candy_pool <= 0:
            context.bot.send_message(update.effective_chat.id, f"Победил компьютер")
            return P4

# def ShowCandyPool(candy_pool):
#     print(f"На столе лежит {candy_pool} конфет \n")
   
# def IsVictory():
#     if candy_pool <= 0:
#         return True
#     else:
#         return False



def StartGame(update, context):
    context.bot.send_message(update.effective_chat.id, f'*** Игра в конфеты  ***\n')
    context.bot.send_message(update.effective_chat.id, f"На столе лежит {max_candy_pool} конфет. Играют два игрока делая ход друг после друга.\nПервый ход делает человек. За один ход можно забрать не более чем {max_candy} конфет.\n")
    return P0


def Error(update, context):
    context.bot.send_message(update.effective_chat.id, f'Что-то пошло не так')

def EndGame(update, context):
    return ConversationHandler.END

# while (candy_pool > 0):
#     roll += 1
#     # context.bot.send_message(update.effective_chat.id, f"-Раунд {roll}-\n")
#     # print(f"-Раунд {roll}-\n")


#     player1_takes_candy = False    
#     while (not player1_takes_candy):
            
#         candy_taken = Player1_Takes_Candy(candy_pool)
#         candy_pool -= candy_taken
#         player1_candy += candy_taken

#         if IsVictory(candy_pool):
#             # context.bot.send_message(update.effective_chat.id, f"Победил игрок\n")
#             # print(f"Победил игрок\n")
#             break

#         candy_taken = Bot_Takes_Candy(candy_pool, rounds_left)
#         candy_pool -= candy_taken
#         player_bot_candy += candy_taken
#         ShowCandyPool(candy_pool)

#         if IsVictory(candy_pool):
#             print(f"Победил компьютер\n")
#             # context.bot.send_message(update.effective_chat.id, f"Победил компьютер\n")
#             break

#         rounds_left -= 1


    

