import pandas as pd


def search_food(keyword, data):

    print(f"Searching for: {keyword}")

    if isinstance(data, str):
        try:
            print(f"Loading data from: {data}")
            db = pd.read_csv(data)
        except FileNotFoundError:
            return "Error: Database file not found."
    else:
        db = data

    keyword_lower = keyword.lower()

    results = db[db['food'].str.lower().str.contains(keyword_lower, na=False)]

    print(f"Found {len(results)} results for {keyword}")

    if results.empty:
        return f"No matches found for keyword: {keyword}"

    return results[['food', 'Fat', 'Carbohydrates', 'Protein', 'Sugars', 'Dietary Fiber', 'Caloric Value']].to_dict(
        orient='records')

import matplotlib.pyplot as plt

def nutrition_breakdown(food_name, data):

    if isinstance(data, str):
        try:
            db = pd.read_csv(data)
        except FileNotFoundError:
            return "Error: Database file not found."
    else:
        db = data

    food_item = db[db['food'].str.lower() == food_name.lower()]

    if food_item.empty:
        return f"Error: {food_name} not found in the database."

    nutrients = ['Caloric Value', 'Fat', 'Carbohydrates', 'Protein', 'Sugars', 'Dietary Fiber']
    values = food_item[nutrients].iloc[0]

    if values.sum() == 0:
        return f"No nutritional data available for {food_name}."

    plt.figure(figsize=(8, 6))
    bars = plt.bar(nutrients, values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.ylabel('Grams')
    plt.title(f'Nutritional Breakdown of {food_name} (in grams)')
    plt.show()

    return f"Nutritional breakdown for {food_name} displayed."



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
            res.append({f"{db['food'].iloc[j]}, {nutrition_name}: {db[nutrition_name].iloc[j]}"})
    return res



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
    top_1 = values_sorted.head(int((0.5*rows)))
    res =[]
    if high:
        for index, value in top_1.items():
            res.append({f"{db['food'][index]}, {nutrition_name}: {value}"})
        return res

    if low:
        values_sorted = db[nutrition_name].sort_values(ascending=True)
        rows = len(values_sorted)
        top_1 = values_sorted.head(int((0.5*rows)))
        for index, value in top_1.items():
            res.append({f"{db['food'][index]}, {nutrition_name}: {value}"})
        return res




