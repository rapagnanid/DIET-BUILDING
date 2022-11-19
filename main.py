from introitocalorico import DailyCalorieIntake
from alimentitabella import df

name = input("Ciao, come ti chiami?: ")

food_list = df['Alimenti'].tolist()

user_input = input("Per favore, inserisci un alimento: ")

filtered_food_list = filter(lambda x: x.startswith(user_input), food_list)

if len(str(filtered_food_list)) > 1:
    print('Ci sono una o più opzioni disponibili per questo alimento:'.format(user_input))
    for index, name in enumerate(filtered_food_list):
        print("{0}".format(name))

food_name = input('Per favore, inserisci nuovamente un alimento, scegliendo tra le possibili opzioni: ')
food_amount = float(input("Qual è la quantità di tale alimento? E.g. (g): "))

calorie_intake = DailyCalorieIntake(name)

print(f"{calorie_intake.name} assumerà: ")
print(calorie_intake.calculator(food_name, food_amount))