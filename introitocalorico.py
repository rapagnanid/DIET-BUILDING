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
    
    calorie = []
    carboidrati = []
    proteine = []
    lipidi = []

    def __init__(self, user_name, food_list_name, food_list_amount):
        self.user_name = user_name
        self.food_list_name = food_list_name
        self.food_list_amount = food_list_amount

    def calculator(self):

        for i in range(0, len(self.food_list_name)):
            self.cal_count[i] = df_def['KCal'][df_def['Alimenti'] == self.food_list_name[i]] * self.food_list_amount[i] / 100
            self.carb_count[i] = df_def['Carboidrati (g)'][df_def['Alimenti'] == self.food_list_name[i]] * self.food_list_amount[i] /100
            self.pro_count[i] = df_def['Proteine (g)'][df_def['Alimenti'] == self.food_list_name[i]] * self.food_list_amount[i] /100
            self.lip_count[i] = df_def['Lipidi (g)'][df_def['Alimenti'] == self.food_list_name[i]] * self.food_list_amount[i] /100

            calorie_totali = sum(self.calorie.append(self.cal_count[i]))
            carboidrati_totali = sum(self.carboidrati.append(self.carb_count[i]))
            proteine_totali = sum(self.proteine.append(self.pro_count[i]))
            lipidi_totali = sum(self.lipidi.append(self.lip_count[i]))


        return pd.DataFrame({
                'KCal': calorie_totali,
                'Carboidrati (g)': carboidrati_totali,
                'Proteine (g)': proteine_totali,
                'Lipidi (g)': lipidi_totali
            })


