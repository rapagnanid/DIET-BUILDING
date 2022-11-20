from alimentitabella import df
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
            cal_count = df[df['Alimenti'] == self.food_list_name[i]]['KCal'] * self.food_list_amount[i] / 100
            self.calorie.append(cal_count)
            carb_count = df[df['Alimenti'] == self.food_list_name[i]]['Carboidrati (g)'] * self.food_list_amount[i] / 100
            self.carboidrati.append(carb_count)
            pro_count = df[df['Alimenti'] == self.food_list_name[i]]['Proteine (g)'] * self.food_list_amount[i] / 100
            self.proteine.append(pro_count)
            lip_count = df[df['Alimenti'] == self.food_list_name[i]]['Lipidi (g)'] * self.food_list_amount[i] / 100
            self.lipidi.append(lip_count)

        return pd.DataFrame({
                'KCal': sum(self.calorie),
                'Carboidrati (g)': sum(self.carboidrati),
                'Proteine (g)': sum(self.proteine),
                'Lipidi (g)': sum(self.lipidi)
            })


