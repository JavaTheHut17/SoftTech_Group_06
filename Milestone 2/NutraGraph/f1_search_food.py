import pandas as pd

def search_food(keyword, data):

    if isinstance(data, str):
        try:
            db = pd.read_csv(data)
        except FileNotFoundError:
            return "Error: Database file not found."
    else:
        db = data

    keyword_lower = keyword.lower()

    results = db[db['food'].str.lower().str.contains(keyword_lower, na=False)]

    if results.empty:
        return f"No matches found for keyword: {keyword}"

    return results['food'].tolist()
