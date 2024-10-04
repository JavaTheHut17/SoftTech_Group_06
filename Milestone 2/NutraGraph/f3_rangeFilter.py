
import pandas as pd

def range_filter(nutri_component, max_n_value, min_n_value, data):

    if not isinstance(max_n_value, (int, float)):
        return print("Error: Min and Max value must be integer or float")

    if not isinstance(min_n_value, (int, float)):
        return print("Error: Min and Max value must be integer or float")

    try:
        db = pd.read_csv(data)
    except:
        return print("Error: DB not found.")

    if nutri_component not in db.columns:
        return print("Error: Nutrient component not found in database")

    nutrition_name = nutri_component

    tf_filter = (min_n_value <= db[nutrition_name]) & (db[nutrition_name] <= max_n_value)
    res =[]
    for j in range(len(tf_filter)):
        if tf_filter[j]:
            res.append(f"{db['food'].iloc[j]}, {nutrition_name}: {db[nutrition_name].iloc[j]}")
    return res


# range_filter('Vitamin D', 300, 200, 'DataBase/Food_Nutrition_Dataset.csv')