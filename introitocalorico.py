from alimentitabella import df_def
import pandas as pd

class DailyCalorieIntake:
    """
    Creates a calorie intake class.
    """

    food_list_name = []
    food_list_amount = []

    cal_count = []
    carb_count = []
    pro_count = []
    lip_count = []

    calorie = 0
    carboidrati = 0
    proteine = 0
    lipidi = 0

    def __init__(self, user_name, food_list_name, food_list_amount):
        self.user_name = user_name
        self.food_list_name = food_list_name
        self.food_list_amount = food_list_amount

    def calculator(self):

        for i in range(0, len(self.food_list_name)):
            self.cal_count.append(int((df_def.loc[df_def['Alimenti'] == self.food_list_name[i], 'KCal'].iloc[0] * self.food_list_amount[i] / 100).round(0)))
            self.carb_count.append(int((df_def.loc[df_def['Alimenti'] == self.food_list_name[i], 'Carboidrati (g)'].iloc[0] * self.food_list_amount[i] / 100).round(0)))
            self.pro_count.append(int((df_def.loc[df_def['Alimenti'] == self.food_list_name[i], 'Proteine (g)'].iloc[0] * self.food_list_amount[i] / 100).round(0)))
            self.lip_count.append(int((df_def.loc[df_def['Alimenti'] == self.food_list_name[i], 'Lipidi (g)'].iloc[0] * self.food_list_amount[i] / 100).round(0)))

        for i in range(0, len(self.cal_count)):
            self.calorie = self.calorie + self.cal_count[i]
        for i in range(0, len(self.carb_count)):
            self.carboidrati = self.carboidrati + self.carb_count[i]
        for i in range(0, len(self.pro_count)):
            self.proteine = self.proteine + self.pro_count[i]
        for i in range(0, len(self.lip_count)):
            self.lipidi = self.lipidi + self.lip_count[i]

        result = {
            'KCal': [self.calorie],
            'Carboidrati (g)': [self.carboidrati],
            'Proteine (g)': [self.proteine],
            'Lipidi (g)': [self.lipidi]
            }

        df_result = pd.DataFrame(result)

        return df_result


