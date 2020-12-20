import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import decimal
from decimal import Decimal

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'args',
    'kwargs',
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_time_it_repetitions_value():
    with pytest.raises(ValueError):
        session5.time_it(print, 1, 2, sep = '-', end = ' ***\n', repetitions = -10)


def test_time_it_repetitions_type():
    with pytest.raises(TypeError):
        session5.time_it(print, 1, 2, sep = '-', end = ' ***\n', repetitions = '25')


def test_squared_power_number_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list, '17', start = 0, end = 5, repetitions = 25)



def test_squared_power_number_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list, -17, start = 0, end = 5, repetitions = 25)



def test_squared_power_start_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list, 17, start = '3', end = 5, repetitions = 25)



def test_squared_power_start_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list, 17, start = -3, end = 5, repetitions = 25)



def test_squared_power_end_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.squared_power_list, 17, start = 0, end = '5', repetitions = 25)



def test_squared_power_end_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.squared_power_list, 17, start = 0, end = 25, repetitions = 25)



def test_polygon_area_side_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.polygon_area, '15', sides = 3, repetitions = 3)



def test_polygon_area_side_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, -15, sides = 3, repetitions = 3)



def test_polygon_area_num_sides_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.polygon_area, 15, sides = 3.0, repetitions = 3)



def test_polygon_area_num_sides_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.polygon_area, 15, sides = 13, repetitions = 3)



def test_temp_converter_temp_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.temp_converter, '30', temp_given_in = 'f', repetitions = 10)



def test_temp_converter_unit_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.temp_converter, 30, temp_given_in = 'k', repetitions = 10)



def test_speed_converter_speed_type():
    with pytest.raises(TypeError):
        session5.time_it(session5.speed_converter, '1000', dist ='km', time ='min', repetitions = 20)



def test_speed_converter_distance_unit_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 1000, dist ='miles', time ='min', repetitions = 20)



def test_speed_converter_time_unit_value():
    with pytest.raises(ValueError):
        session5.time_it(session5.speed_converter, 1000, dist ='km', time ='lightyears', repetitions = 20)



def test_squared_power_list():
    assert [27, 81, 243] == session5.squared_power_list(3, start = 3, end = 5)



def test_polygon_area_calculation():
    assert 97.42785792574938 == session5.polygon_area(15, sides = 3)



def test_temp_converter_calculation():
    assert 0 == session5.temp_converter(32, temp_given_in = 'f')



def test_speed_converter_kmperday():
    assert 24 == session5.speed_converter(1, dist='km', time='day')



def test_speed_converter_kmpersec():
    assert 0.3 == session5.speed_converter(1000, dist='km', time='s')



def test_speed_converter_kmperms():
    assert 0.3 == session5.speed_converter(1e6, dist='km', time='ms')



def test_speed_converter_kmpermin():
    assert 1.7 == session5.speed_converter(100, dist='km', time='min')



def test_speed_converter_kmperhr():
    assert 15 == session5.speed_converter(15, dist='km', time='hr')



def test_speed_converter_mperhr():
    assert 1000 == session5.speed_converter(1, dist='m', time='hr')



def test_speed_converter_ftperhr():
    assert 3280.8 == session5.speed_converter(1, dist='ft', time='hr')



def test_speed_converter_yrdperhr():
    assert 1093.6 == session5.speed_converter(1, dist='yrd', time='hr')