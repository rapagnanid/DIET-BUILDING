import pandas as pd
from introitocalorico import DailyCalorieIntake
from alimentitabella import df

check_food_list = df['Alimenti'].tolist()
#food_name = []
#food_amount = []

stop = 'STOP'
fatto = 'FATTO'

name = input("Ciao, come ti chiami?: ")
while True:
    user_input = input("Per favore, inserisci un alimento: ")
    filtered_food_list = filter(lambda x: x.startswith(user_input), check_food_list)
    if len(str(filtered_food_list)) > 1:
        print('Ci sono una o più opzioni disponibili per questo alimento:'.format(user_input))
        for index, name in enumerate(filtered_food_list):
            print("{0}".format(name))
    food_name = input('Per favore, inserisci nuovamente un alimento, scegliendo tra le possibili opzioni: ')
    food_amount = float(input('Per favore, inserisci la quantità di tale alimento (g): '))
    #inputed_food_list = [].append(food_name, food_amount)
    next_action = input('Per favore, premi ENTER per continuare, altrimenti digita FATTO per andare al calcolo oppure STOP terminare: ')
    if next_action == fatto:
        calorie_intake = DailyCalorieIntake(name)
        print(f"{calorie_intake.name} assumerà giornalmente: ")
        print(calorie_intake.calculator(food_name, food_amount))
        break
    elif next_action == stop:
        break


