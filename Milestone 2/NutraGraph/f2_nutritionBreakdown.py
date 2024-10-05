import pandas as pd
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

    nutrients = ['Fat', 'Carbohydrates', 'Protein', 'Sugars', 'Dietary Fiber']
    values = food_item[nutrients].iloc[0]

    if values.sum() == 0:
        return f"No nutritional data available for {food_name}."

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=nutrients, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
    plt.title(f'Nutritional Breakdown of {food_name}')
    plt.axis('equal')
    plt.show()

    return f"Nutritional breakdown for {food_name} displayed."
