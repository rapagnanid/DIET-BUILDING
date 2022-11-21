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

    def __init__(self, user_name, food_list_name, food_list_amount):
        self.user_name = user_name
        self.food_list_name = food_list_name
        self.food_list_amount = food_list_amount

    def calculator(self):

        for i in range(0, len(self.food_list_name)):

            self.cal_count.append(df_def[df_def['Alimenti'] == self.food_list_name[i]].loc[:, 'KCal'] * self.food_list_amount[i] / 100)
            self.carb_count.append(df_def[df_def['Alimenti'] == self.food_list_name[i]].loc[:, 'Carboidrati (g)'] * self.food_list_amount[i] / 100)
            self.pro_count.append(df_def[df_def['Alimenti'] == self.food_list_name[i]].loc[:, 'Proteine (g)'] * self.food_list_amount[i] / 100)
            self.lip_count.append(df_def[df_def['Alimenti'] == self.food_list_name[i]].loc[:, 'Lipidi (g)'] * self.food_list_amount[i] / 100)

        """for i, val in range(0, len(self.cal_count)):
            calorie = sum(self.cal_count[i])
        for i in self.carb_count:
            carboidrati = sum(self.carb_count[i])
        for i in self.pro_count:
            proteine = sum(self.pro_count[i])
        for i in self.lip_count:
            lipidi = sum(self.lip_count[i])"""

        return self.cal_count #pd.DataFrame({
                #'KCal': sum(self.cal_count),
                #'Carboidrati (g)': sum(self.carb_count),
                #'Proteine (g)': sum(self.pro_count),
                #'Lipidi (g)': sum(self.lip_count)
            #})
