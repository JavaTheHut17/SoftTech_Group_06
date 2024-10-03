

import pytest
from f3_rangeFilter import range_filter

def test_range_filter():

    db = 'DataBase/Food_Nutrition_Dataset.csv'


    range_filter('Vitamin E', 0.08, 0.07, db)

