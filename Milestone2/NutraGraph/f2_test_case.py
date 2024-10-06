import pytest
import pandas as pd
from f2_nutritionBreakdown import nutrition_breakdown

db = pd.read_csv('DataBase/Food_Nutrition_Dataset.csv')

def test_nutrition_breakdown_valid_food():
    result = nutrition_breakdown('cream cheese', db)
    assert result == "Nutritional breakdown for cream cheese displayed."

def test_nutrition_breakdown_invalid_food():
    result = nutrition_breakdown('slurpee', db)
    assert result == "Error: slurpee not found in the database."


def test_nutrition_breakdown_invalid_db():
    result = nutrition_breakdown('cream cheese', 'Invalid_DB.csv')
    assert result == "Error: Database file not found."
