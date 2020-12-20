import pytest
import session7
import os
import inspect
import re
from session7 import *

README_CONTENT_CHECK_FOR = [
    'Fibonacci',
    'lambda',
    'vowel',
    'ReLU',
    'sigmoid',
    'shifts characters',
    'swear words',
    'reduce',
    'biggest character',
    'number plates',
    'partial'
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
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_fibonacci():
    assert check_fibonacci([1, 5, 333, 777, 1597, 6765, 8000]) == [1, 5, 1597, 6765], "check_fibonacci is not correctly implemented!"


def test_add_even_odd():
    assert add_even_odd([4, 7, 10, 15, 20], [3, 6, 8, 1, 11]) == [7, 31], "add_even_odd is not correctly implemented!"


def test_add_even_corner_case():
    assert add_even_odd([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == [], "add_even_odd corner case not handled!"


def test_strip_vowels():
    assert strip_vowels('tsai') == ['t', 's'], "strip_vowels is not correctly implemented!"


def test_relu_func():
    assert relu_func([1.43, -0.76, 0.356, -1.89]) == [1.43, 0, 0.356, 0], "relu_func is not correctly implemented!"


def test_sigmoid_func():
    assert sigmoid_func([1, 2, -3, -4, 0]) == [0.7310585786300049, 0.8807970779778823, 0.04742587317756678, 0.01798620996209156, 0.5], "sigmoid_func is not correctly implemented!"


def test_shift_characters():
    assert shift_characters('tsai') == 'yxfn', "shift_characters is not correctly implemented!"
    assert shift_characters('zero') == 'ejwt', "shift_characters is not correctly implemented!"


def test_swear_words():
    user_input1 = """Goa Chief Minister Pramod Sawant on Sunday said an asswhole insurance cover of ₹50 lakh has been extended to all health workers who are at the forefront of the battle against COVID-19.
    The insurance cover is provided under the central governments flagship Pradhan Mantri Garib Kalyan Yojana. 
    “Insurance cover of ₹50 lakh has been extended to all health workers in Goa,” Mr. Sawant tweeted. 
    The Pradhan Mantri Garib Kalyan Yojana provides an insurance cover of ₹50 lakh per health worker in case of loss of life due to COVID-19 or accidental loss of life on account of coronavirus-related duties, he said.
    The scheme is funded through the National Disaster Response Fund, operated by the Ministry of Health and Family Welfare."""

    user_input2 = """Goa Chief Minister Pramod Sawant on Sunday said an insurance cover of ₹50 lakh has been extended to all health workers who are at the forefront of the battle against COVID-19.
    The insurance cover is provided under the central governments flagship Pradhan Mantri Garib Kalyan Yojana. 
    “Insurance cover of ₹50 lakh has been extended to all health workers in Goa,” Mr. Sawant tweeted. 
    The Pradhan Mantri Garib Kalyan Yojana provides an insurance cover of ₹50 lakh per health worker in case of loss of life due to COVID-19 or accidental loss of life on account of coronavirus-related duties, he said.
    The scheme is funded through the National Disaster Response Fund, operated by the Ministry of Health and Family Welfare."""

    assert check_swear_words(user_input1) == True, "check_swear_words is not correctly implemented!"
    assert check_swear_words(user_input2) == False, "check_swear_words is not correctly implemented!"


def test_add_even_numbers():
    assert add_even_numbers([10, 15, 17, 20, 33, 40]) == 70, "add_even_numbers is not correctly implemented!"


def test_add_even_numbers_corner_case():
    assert add_even_numbers([19, 15, 17, 25, 33, 41]) == 0, "add_even_numbers is not correctly implemented!"


def test_find_biggest_character():
    assert find_biggest_character("SomaKorada") == 'r', "find_biggest_character is not correctly implemented!"


def test_add_third_element():
    assert add_third_element([1, 2, 3, 4, 5, 6]) == 9, "add_third_element is not correctly implemented!"


def test_add_third_element_corner_case():
    assert add_third_element([1, 2]) == 0, "add_third_element corner case is not handled!"


def test_generate_number_plate():
    assert all([x[:2]=="KA" and (int(x[2:4]) in range(10, 100)) and (int(x[-4:]) in range(1000, 10000)) for x in generate_number_plate()])


def test_random_plates():
    assert all([x[:2]=="DL" and int(x[2:4]) in range(10, 100) and int(x[-4:]) == 7777 for x in random_plates('DL', 7777)])








