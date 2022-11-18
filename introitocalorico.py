from alimentitabella import df

class DailyCalorieIntake:
    """
    Creates a calorie intake class.
    """

    def __init__(self, name):
        self.name = name

    def calculator(self, food_name, food_amount):

        alimento = df[df['Alimenti']==food_name]

        alimento_nutrienti = alimento.loc[ : , alimento.columns != 'Alimenti']

        return alimento_nutrienti * food_amount / 100
