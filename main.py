import pandas as pd
from introitocalorico import DailyCalorieIntake
from alimentitabella import df

check_food_list = df['Alimenti'].tolist()
#food_name = []
#food_amount = []

i = 'STOP'

name = input("Ciao, come ti chiami?: ")
while True:
    user_input = input("Per favore, inserisci un alimento, oppure digita STOP per uscire: ")
    if user_input == i:
        break
    else:
        filtered_food_list = filter(lambda x: x.startswith(user_input), check_food_list)
        if len(str(filtered_food_list)) > 1:
            print('Ci sono una o più opzioni disponibili per questo alimento:'.format(user_input))
            for index, name in enumerate(filtered_food_list):
                print("{0}".format(name))
        food_name = input('Per favore, inserisci nuovamente un alimento, scegliendo tra le possibili opzioni, oppure digita STOP per uscire: ')
        if food_name == i:
            break
        else:
            food_amount = float(input("Qual è la quantità di tale alimento? E.g. (g): "))

            calorie_intake = DailyCalorieIntake(name)

            print(f"{calorie_intake.name} assumerà: ")
            print(calorie_intake.calculator(food_name, food_amount))