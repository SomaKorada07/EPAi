import pytest
import session10
import os
import inspect
import re
from random import randint
from session10 import *

README_CONTENT_CHECK_FOR = [
    'namedtuple',
    'stock',
    'exchange',
    'index',
    'fake profiles',
    'dictionary',
    'Faker',
    'immutable',
    'runtime',
    'age',
    'location',
    'blood'
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
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  



def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__



def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        if function[1].__name__ not in ['namedtuple', 'wraps']:
            assert function[1].__annotations__



def test_generate_fake_profiles_np():
    fake_profiles = generate_fake_profiles_np(100)
    assert len(fake_profiles) == 100, "Something wrong with the generate_fake_profiles_np function."
    assert fake_profiles[randint(0, 99)]._fields == tuple((faker.profile()).keys()), "Something wrong with the generate_fake_profiles_np function."



def test_generate_fake_profiles_dict():
    fake_profiles = generate_fake_profiles_dict(100)
    assert len(fake_profiles) == 100, "Something wrong with the generate_fake_profiles_dict function."
    assert sorted(list(fake_profiles[randint(0, 99)].keys())) == sorted(list((faker.profile()).keys())), "Something wrong with the generate_fake_profiles_dict function."