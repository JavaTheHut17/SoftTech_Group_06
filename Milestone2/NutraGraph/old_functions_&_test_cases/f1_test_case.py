import pytest
import pandas as pd
from f1_search_food import search_food

db = pd.read_csv(
    '../../../../../../../../../../../Library/CloudStorage/GoogleDrive-lukehewitt1717@gmail.com/My Drive/Documents/07_Study/02_Bachelor Of Information Technology/Tri_2_2024/02_2810ICT_Software Tech/Assignment_01/SoftTech_Group_06/Milestone2/NutraGraph/DataBase/Food_Nutrition_Dataset.csv')

def test_search_food_keyword_found():
    expect_res = ['watermelon', 'watermelon seed kernels dried']

    func_res = search_food('watermelon', db)

    assert func_res == expect_res

def test_search_food_keyword_partial_match():
    expect_res = ['surimi', 'surinam cherry pitanga']

    func_res = search_food('suri', db)

    assert func_res == expect_res

def test_search_food_keyword_not_found():
    expect_res = "No matches found for keyword: slurpee"

    func_res = search_food('slurpee', db)

    assert func_res == expect_res

def test_search_food_invalid_db():
    expect_res = "Error: Database file not found."

    func_res = search_food('cheese', 'Invalid_DB.csv')

    assert func_res == expect_res
