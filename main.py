from introitocalorico import DailyCalorieIntake
from alimentitabella import df

check_food_list = df['Alimenti'].tolist()

food_list_name = []
food_list_amount = []

stop = 'STOP'
fatto = 'FATTO'

user_name = input("Ciao, come ti chiami?: ")

while True:
    user_input = input("Per favore, inserisci un alimento: ")
    filtered_food_list = filter(lambda x: x.startswith(user_input), check_food_list)

    if len(str(filtered_food_list)) > 1:
        print('Ci sono una o più opzioni disponibili per questo alimento:'.format(user_input))

        for index, name in enumerate(filtered_food_list):
            print("{0}".format(name))

    food_name = input('Per favore, inserisci nuovamente un alimento, scegliendo tra le possibili opzioni: ')
    food_list_name.append(food_name)
    food_amount = float(input('Per favore, inserisci la quantità di tale alimento (g): '))
    food_list_amount.append(food_amount)

    next_action = input('Per favore, premi ENTER per continuare, altrimenti digita FATTO per andare al calcolo oppure STOP terminare: ')

    if next_action == fatto:
        print(food_list_name)
        print(food_list_amount)
        calorie_intake = DailyCalorieIntake(user_name=user_name, food_list_name=food_list_name, food_list_amount=food_list_amount)
        print(f"{calorie_intake.user_name} assumerà giornalmente: ")
        print(calorie_intake.calculator())
        break

    elif next_action == stop:
        break
