import pytest
import session8
import os
import inspect
import re
from session8 import *

README_CONTENT_CHECK_FOR = [
    'docstring',
    'free variable',
    'Fibonacci',
    'closure',
    'counts',
    'global dictionary',
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
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_docstring_closure_standard():
    f = check_docstring(int)
    assert f(), "Function passed does not have sufficient docstring!"


def test_docstring_closure_custom():
    f = next_fibonacci()
    assert check_docstring(f), "Function passed does not have sufficient docstring!"


def test_next_fibonacci():
    f = next_fibonacci()
    assert f() == 1, "next_fibonacci is not implemented correctly!"
    assert f() == 2, "next_fibonacci is not implemented correctly!"
    assert f() == 3, "next_fibonacci is not implemented correctly!"
    assert f() == 5, "next_fibonacci is not implemented correctly!"
    assert f() == 8, "next_fibonacci is not implemented correctly!"


def test_fn_counter():
    counter_add = fn_counter(add)
    counter_mult = fn_counter(mul)
    counter_add(1, 2)
    counter_add(3, 4)
    assert func_counter == {'add': 2}, "fn_counter is not implemented correctly!"
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    assert func_counter == {'add': 2, 'mul': 5}, "fn_counter is not implemented correctly!"


def test_fn_user_counter():
    user1_counter = {'add': 2, 'mul': 5}
    counter_add = fn_user_counter(add, user1_counter)
    counter_mult = fn_user_counter(mul, user1_counter)
    counter_add(1, 2)
    counter_add(3, 4)
    assert user1_counter == {'add': 4, 'mul': 5}, "fn_counter is not implemented correctly!"
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    assert user1_counter == {'add': 4, 'mul': 10}, "fn_counter is not implemented correctly!"

    user2_counter = {'add': 10, 'mul': 5}
    counter_add = fn_user_counter(add, user2_counter)
    counter_mult = fn_user_counter(mul, user2_counter)
    counter_add(1, 2)
    counter_add(3, 4)
    assert user2_counter == {'add': 12, 'mul': 5}, "fn_counter is not implemented correctly!"
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    counter_mult(2, 5)
    assert user2_counter == {'add': 12, 'mul': 10}, "fn_counter is not implemented correctly!"
