
import pandas as pd


def range_filter():

    db = pd.read_csv("DataBase/Food_Nutrition_Dataset.csv")

    options = [
        'Caloric Value', 'Fat', 'Saturated Fats', 'Monounsaturated Fats',
        'Polyunsaturated Fats', 'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber',
        'Cholesterol', 'Sodium', 'Water', 'Vitamin A', 'Vitamin B1', 'Vitamin B11',
        'Vitamin B12', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6',
        'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Calcium', 'Copper',
        'Iron', 'Magnesium', 'Manganese', 'Phosphorus', 'Potassium', 'Selenium',
        'Zinc', 'Nutrition Density'
        ]

# print(enumerate(options))
    for i, listOption in enumerate(options): print(i, listOption)

    nutri_component = int(input("Enter Nutrient Component number : "))
    max_n_value = float(input("Enter Max_Value : "))
    min_n_value = float(input("Enter Min_Value : "))

    selection = nutri_component

    nutrition_name = options[selection]

    tf_filter = (min_n_value <= db[nutrition_name]) & (db[nutrition_name] <= max_n_value)

    for j in range(len(tf_filter)):
        if tf_filter[j]:
            print(f"{db['food'].iloc[j]}, {nutrition_name}: {db[nutrition_name].iloc[j]}")


range_filter()