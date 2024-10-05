
import pytest
from f5_high_low_filter import high_low_filter

def test_high_low_filter_db_error():

    expect_res = print("Error: DB not found.")

    func_res = high_low_filter('Vitamin D', high = False, low = True, data = 'DataBase/Food_Nutrition_Datasets.csv')

    assert func_res == expect_res


def test_high_low_filter_low():

    func_res = high_low_filter('Vitamin D', high = False, low = True, data = 'DataBase/Food_Nutrition_Dataset.csv')

    expect_res = [{'cream cheese, Vitamin D: 0.0'}, {'fruit flavored water, Vitamin D: 0.0'}, {'table water, Vitamin D: 0.0'}, {'tap water, Vitamin D: 0.0'}, {'water dannon, Vitamin D: 0.0'}, {'grape juice, Vitamin D: 0.0'}, {'lime juice, Vitamin D: 0.0'}, {'apple juice martinellis, Vitamin D: 0.0'}, {'apple juice concentrate, Vitamin D: 0.0'}, {'acerola cherry juice, Vitamin D: 0.0'}, {'white grapefruit juice, Vitamin D: 0.0'}, {'orange pineapple juice, Vitamin D: 0.0'}, {'fruchtcocktail granini, Vitamin D: 0.0'}, {'orangensaft ja, Vitamin D: 0.0'}, {'water, Vitamin D: 0.0'}, {'apricot nectar, Vitamin D: 0.0'}, {'horchata, Vitamin D: 0.0'}, {'guanabana nectar, Vitamin D: 0.0'}, {'prune juice, Vitamin D: 0.0'}, {'citrus fruit juice, Vitamin D: 0.0'}, {'cranberry grape juice, Vitamin D: 0.0'}, {'blackberry juice, Vitamin D: 0.0'}, {'pineapple orange juice, Vitamin D: 0.0'}]

    assert func_res == expect_res

def test_high_low_filter_high():

    func_res = high_low_filter('Vitamin D', high = True, low = False, data = 'DataBase/Food_Nutrition_Dataset.csv')

    expect_res = [{'pokeberry shoots raw, Vitamin D: 217.6'}, {'broccoli cooked, Vitamin D: 181.7'}, {'tomato juice, Vitamin D: 170.3'}, {'kohlrabi raw, Vitamin D: 164.3'}, {'guava, Vitamin D: 125.6'}, {'mango, Vitamin D: 122.3'}, {'pineapple juice, Vitamin D: 109.5'}, {'green chili pepper, Vitamin D: 109.1'}, {'nance, Vitamin D: 103.6'}, {'cabbage raw, Vitamin D: 102.5'}, {'orange juice, Vitamin D: 100.0'}, {'orange, Vitamin D: 97.9'}, {'lemon juice, Vitamin D: 94.4'}, {'grapefruit juice, Vitamin D: 93.9'}, {'kohlrabi cooked, Vitamin D: 89.1'}, {'papaya, Vitamin D: 88.3'}, {'broccoli raw, Vitamin D: 81.2'}, {'acerola cherry, Vitamin D: 80.5'}, {'tangerine juice, Vitamin D: 76.6'}, {'pummelo, Vitamin D: 76.3'}, {'peach nectar, Vitamin D: 75.2'}, {'pear nectar, Vitamin D: 67.5'}, {'vegetable juice, Vitamin D: 67.0'}]

    assert func_res == expect_res

def test_high_low_filter():

    func_res = high_low_filter('Vitamin P', high = True, low = False, data = 'DataBase/Food_Nutrition_Dataset.csv')

    expect_res = print("Error: Nutrient component not found in database")

    assert func_res == expect_res