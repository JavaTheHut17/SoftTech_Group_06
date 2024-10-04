

import pandas as pd

def high_med_low_filter(nutri_component,high,med,low,data):

    try:
        db = pd.read_csv(data)
    except:
        return print("Error: DB not found.")

    if nutri_component not in db.columns:
        return print("Error: Nutrient component not found in database")

    nutrition_name = nutri_component

    low_value = db[nutrition_name].max() * .33
    high_value = db[nutrition_name].max() * .66

    if high:
        value_filter = (db[nutrition_name] >= high_value)
        res = []
        for i in range(len(value_filter)):
            if value_filter[i]:
                res.append({f"{db['food'].iloc[i]}, {nutrition_name}: {db[nutrition_name].iloc[i]}"})
        return res

    if med:
        value_filter = (db[nutrition_name] >= low_value) & (db[nutrition_name] <= high_value)
        res = []
        for i in range(len(value_filter)):
            if value_filter[i]:
                res.append({f"{db['food'].iloc[i]}, {nutrition_name}: {db[nutrition_name].iloc[i]}"})
        return res

    if low:
        value_filter = db[nutrition_name] <= low_value
        res = []
        for i in range(len(value_filter)):
            if value_filter[i]:
                res.append({f"{db['food'].iloc[i]}, {nutrition_name}: {db[nutrition_name].iloc[i]}"})
        return res


# high_med_low_filter('Vitamin D', high=False, med=True, low=False, data='DataBase/Food_Nutrition_Dataset.csv')





