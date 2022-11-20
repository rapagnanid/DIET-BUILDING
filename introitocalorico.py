from alimentitabella import df_def
import pandas as pd

class DailyCalorieIntake:
    """
    Creates a calorie intake class.
    """

    food_list_name = []
    food_list_amount = []
    
    calorie = []
    carboidrati = []
    proteine = []
    lipidi = []

    def __init__(self, user_name, food_list_name, food_list_amount):
        self.user_name = user_name
        self.food_list_name = food_list_name
        self.food_list_amount = food_list_amount

    def calculator(self):

        for i in range(len(self.food_list_name)):
            cal_count = df_def[df_def['Alimenti'] == self.food_list_name[i]]['KCal'] * self.food_list_amount[i]
            carb_count = df_def[df_def['Alimenti'] == self.food_list_name[i]]['Carboidrati (g)'] * self.food_list_amount[i]
            pro_count = df_def[df_def['Alimenti'] == self.food_list_name[i]]['Proteine (g)'] * self.food_list_amount[i]
            lip_count = df_def[df_def['Alimenti'] == self.food_list_name[i]]['Lipidi (g)'] * self.food_list_amount[i]

            calorie_totali = pd.DataFrame(self.calorie.append(cal_count)).sum(axis=0)
            carboidrati_totali = pd.DataFrame(self.carboidrati.append(carb_count)).sum(axis=0)
            proteine_totali = pd.DataFrame(self.proteine.append(pro_count)).sum(axis=0)
            lipidi_totali = pd.DataFrame(self.lipidi.append(lip_count)).sum(axis=0)


        return pd.DataFrame({
                'KCal': calorie_totali,
                'Carboidrati (g)': carboidrati_totali,
                'Proteine (g)': proteine_totali,
                'Lipidi (g)': lipidi_totali
            })


