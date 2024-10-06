import pytest
import pandas as pd
from f2_nutritionBreakdown import nutrition_breakdown

db = pd.read_csv(
    '../../../../../../../../../../../Library/CloudStorage/GoogleDrive-lukehewitt1717@gmail.com/My Drive/Documents/07_Study/02_Bachelor Of Information Technology/Tri_2_2024/02_2810ICT_Software Tech/Assignment_01/SoftTech_Group_06/Milestone2/NutraGraph/DataBase/Food_Nutrition_Dataset.csv')

def test_nutrition_breakdown_valid_food():
    result = nutrition_breakdown('cream cheese', db)
    assert result == "Nutritional breakdown for cream cheese displayed."

def test_nutrition_breakdown_invalid_food():
    result = nutrition_breakdown('slurpee', db)
    assert result == "Error: slurpee not found in the database."


def test_nutrition_breakdown_invalid_db():
    result = nutrition_breakdown('cream cheese', 'Invalid_DB.csv')
    assert result == "Error: Database file not found."
