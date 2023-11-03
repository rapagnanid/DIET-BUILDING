# Import required module
from fitness_tools.meals.meal_maker import MakeMeal

# Create object
obj = MakeMeal(160, goal='weight_gain', activity_level='moderate',
			body_type='mesomorph')

# Traverse each object
print(obj.daily_max_calories())
print(obj.daily_min_fat())
print(obj.daily_max_protein())
print(obj.daily_min_carbs())
print(obj.daily_max_carbs())

# Return calories and macronutrients
# for one meal.
print(obj.make_meal(4))
