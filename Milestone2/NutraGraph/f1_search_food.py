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
