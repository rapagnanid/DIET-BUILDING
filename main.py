from introitocalorico import DailyCalorieIntake
from alimentitabella import df
import inquirer

food_list = df['Alimenti'].to_list()

questions = [
  inquirer.List('size',
                message="Quale alimento vuoi considerare nel calcolo?",
                choices=food_list,
            ),
]
answers = inquirer.prompt(questions)
print(answers["size"])

"""
name = input("Come ti chiami?: ")
food_name = input("Quale alimento vuoi considerare nel calcolo?: ")
food_amount = float(input("Qual è la quantità di tale alimento che vuoi considerare nel calcolo? E.g. (g): "))

name, age, score = input("Enter student's name, age and score separated by space:").split()


entered_list = input("Enter a list of numbers separated by space: ").split()
print('Intermediate_list: ',entered_list)

num_list = list(map(int,entered_list))

calorie_intake = DailyCalorieIntake(name)

print(f"{calorie_intake.name} assumerà: ")
print(calorie_intake.calculator(food_name, food_amount))
"""
