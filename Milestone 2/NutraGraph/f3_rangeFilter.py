
import pandas as pd


def range_filter(nutri_component, max_n_value, min_n_value, data):

    db = pd.read_csv(data)

    nutrition_name = nutri_component

    tf_filter = (min_n_value <= db[nutrition_name]) & (db[nutrition_name] <= max_n_value)
    res =[]
    for j in range(len(tf_filter)):
        if tf_filter[j]:
            res.append(f"{db['food'].iloc[j]}, {nutrition_name}: {db[nutrition_name].iloc[j]}")

    return print(res)

range_filter('Vitamin E', 0.08, 0.079, 'DataBase/Food_Nutrition_Dataset.csv')