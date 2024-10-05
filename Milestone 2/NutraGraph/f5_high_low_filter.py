

import pandas as pd

def high_low_filter(nutri_component, high, low, data):

    try:
        db = pd.read_csv(data)
    except:
        return print("Error: DB not found.")

    if nutri_component not in db.columns:
        return print("Error: Nutrient component not found in database")

    nutrition_name = nutri_component
    values_sorted = db[nutrition_name].sort_values(ascending=False)
    rows = len(values_sorted)
    top_1 = values_sorted.head(int((0.01*rows)))
    res =[]
    if high:
        for index, value in top_1.items():
            res.append({f"{db['food'][index]}, {nutrition_name}: {value}"})
        return res

    if low:
        values_sorted = db[nutrition_name].sort_values(ascending=True)
        rows = len(values_sorted)
        top_1 = values_sorted.head(int((0.01*rows)))
        for index, value in top_1.items():
            res.append({f"{db['food'][index]}, {nutrition_name}: {value}"})
        return res


# high_low_filter('Vitamin D', high = True, low = False, data = 'DataBase/Food_Nutrition_Dataset.csv')