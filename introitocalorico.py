from alimentitabella import df
import pandas as pd

class DailyCalorieIntake:
    """
    Creates a calorie intake class.
    """
    df_food_inputed = pd.DataFrame()

    calorie = []
    carboidrati = []
    proteine = []
    lipidi = []

    def __init__(self, user_name, food_list_name, food_list_amount):
        self.user_name = user_name
        self.food_list_name = food_list_name
        self.food_list_amount = food_list_amount

    def calculator(self):

        self.df_food_inputed = pd.DataFrame({
            'food_name': self.food_list_name,
            'food_amount': self.food_list_amount
        })

        for i in self.df_food_inputed['food_name']:
            cal_count = df[df['Alimenti'] == self.df_food_inputed['food_name']]['KCal'] * self.df_food_inputed['food_amount'] / 100
            self.calorie.append(cal_count)
            carb_count = df[df['Alimenti'] == self.df_food_inputed['food_name']]['Carboidrati (g)'] * self.df_food_inputed['food_amount'] / 100
            self.carboidrati.append(carb_count)
            pro_count = df[df['Alimenti'] == self.df_food_inputed['food_name']]['Proteine (g)'] * self.df_food_inputed['food_amount'] / 100
            self.proteine.append(pro_count)
            lip_count = df[df['Alimenti'] == self.df_food_inputed['food_name']]['Proteine (g)'] * self.df_food_inputed['food_amount'] / 100
            self.lipidi.append(lip_count)

        return pd.DataFrame({
                'KCal': sum(self.calorie),
                'Carboidrati (g)': sum(self.carboidrati),
                'Proteine (g)': sum(self.proteine),
                'Lipidi (g)': sum(self.lipidi)
            })


