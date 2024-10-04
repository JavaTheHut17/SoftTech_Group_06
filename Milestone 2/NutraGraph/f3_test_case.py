

import pytest
from f3_rangeFilter import range_filter

def test_range_filter():

    db = 'DataBase/Food_Nutrition_Dataset.csv'

    expect_res = ['rice bowl with chicken, Vitamin E: 0.08', 'strawberry topping, Vitamin E: 0.079',
                  'instant white rice raw, Vitamin E: 0.079', 'strawberries, Vitamin E: 0.079',
                  'sage ground, Vitamin E: 0.08', 'navy beans raw, Vitamin E: 0.08',
                  'navy beans cooked, Vitamin E: 0.08', 'veal thymus cooked, Vitamin E: 0.079',
                  'fruit yogurt, Vitamin E: 0.079', 'instant cappuccino powder, Vitamin E: 0.08',
                  'pineapple orange juice, Vitamin E: 0.079', 'chestnuts roasted, Vitamin E: 0.08',
                  'hot chile pepper dried, Vitamin E: 0.079', 'dried tomatoes, Vitamin E: 0.079',
                  'shiitake mushrooms cooked, Vitamin E: 0.08']

    func_res = range_filter('Vitamin E', 0.08, 0.079, db)

    assert func_res == expect_res

def test_range_filter_no_res():

    expect_res = []

    func_res = range_filter('Vitamin D', 300, 230, 'DataBase/Food_Nutrition_Dataset.csv')

    assert func_res == expect_res

def test_range_filter_invalid_name():

    expect_res = print("Error: Nutrient component not found in database")

    func_res = range_filter('Vitamin Q', 300, 230, 'DataBase/Food_Nutrition_Dataset.csv')

    assert func_res == expect_res

def test_range_filter_invalid_value():

    expect_res = print("Error: Min and Max value must be integer or float")

    func_res = range_filter('Vitamin E', '300', 230, 'DataBase/Food_Nutrition_Dataset.csv')

    assert func_res == expect_res

def test_range_filter_invalid_value2():

    expect_res = print("Error: Min and Max value must be integer or float")

    func_res = range_filter('Vitamin E', 300, '230', 'DataBase/Food_Nutrition_Dataset.csv')

    assert func_res == expect_res

def test_range_filter_no_db():

    expect_res = print("Error: DB not found.")

    func_res = range_filter('Vitamin E', 300, 230, 'DataBase')

    assert func_res == expect_res

