import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import decimal
from decimal import Decimal
from session4 import Qualean
from math import copysign

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__',
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
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_wrong_qualean():
    with pytest.raises(ValueError) as err:
        q = Qualean(3)


def test_qualean_instance():
    q = Qualean(1)
    assert isinstance(q, Qualean)


def test_qualean_value():
    q1 = Qualean(1)
    q2 = Qualean(0)
    q3 = Qualean(-1)
    assert q1.number >= -1 and q1.number <= 1
    assert q2.number == 0
    assert q3.number >= -1 and q1.number <= 1



def test_number_of_fractional_digits():
    q = Qualean(1)
    assert len(str(q).split(".")[-1]) == 10



def test_qualean_repr():
    s = Qualean(1)

    assert 'object at' not in s.__repr__()


def test_qualean_str():
    s = Qualean(1)

    assert s.__str__() == str(s.number)


def test_qualean_and():
    q1 = Qualean(1)
    q2 = Qualean(0)
    q3 = Qualean(-1)
    i = 113

    if q1 and q3:
        assert q1.__and__(q3)
    assert not q1.__and__(q2)
    assert not q3.__and__(q2)
    assert not q2.__and__(i)


def test_qualean_or():
    q1 = Qualean(1)
    q2 = Qualean(0)
    q3 = Qualean(-1)
    i = 113

    if q1 or q3:
        assert q1.__or__(q3)
    assert q1.__or__(q2)
    assert q3.__or__(q2)
    if q1:
        assert q1.__or__(i)


def test_qualean_add():
    q1, q2 = Qualean(1), Qualean(-1)

    assert q1 + q2 == q1.number + q2.number


def test_qualean_eq():
    q1, q2 = Qualean(0), Qualean(0)

    assert q1 == q2


def test_qualean_float():
    q1 = Qualean(1)

    assert isinstance(float(q1), float)


def test_qualean_invertsign():
    q = Qualean(1)
    y = q.number

    assert -q.number + y == 0


def test_qualean_ge():
    q1, q2, q3 = Qualean(1), Qualean(0), Qualean(0)

    if q1.number < 0:
        q1 = q1.__invertsign__()

    assert q1 >= q2
    assert q2 >= q3


def test_qualean_gt():
    q1, q2 = Qualean(1), Qualean(0)
    
    if q1.number < 0:
        q1 = q1.__invertsign__()

    assert q1 > q2


def test_qualean_lt():
    q1, q2 = Qualean(1), Qualean(0)

    if q1.number > 0:
        q1 = q1.__invertsign__()

    assert q1 < q2


def test_qualean_le():
    q1, q2, q3 = Qualean(1), Qualean(0), Qualean(0)

    if q1.number > 0:
        q1 = q1.__invertsign__()

    assert q1 <= q2
    assert q2 <= q3


def test_qualean_mul():
    q1, q2 = Qualean(1), Qualean(-1)

    assert q1 * q2 == q1.number * q2.number


def test_qualean_sqrt():
    decimal.getcontext().prec = 10
    sign = lambda x : copysign(1.0, x)
    q = Qualean(-1)

    if q.number < 0:
        q = q.__invertsign__()

    assert q.__sqrt__() == Decimal(q.number).sqrt()


def test_qualean_bool():
    s = Qualean(0)

    assert not s.__bool__()


def test_repetitive_addition_multiplication():
    q = Qualean(random.choice([0, -1, 1]))
    res = 0

    for _ in range(0, 100):
        res += q.number

    assert round(res,10) == round(100 * q.number,10)


def test_million_q_sum():
    result = 0

    for _ in range(0,1000000):
        x = random.choice([0, -1, 1])
        result += Qualean(x).number

    assert math.isclose(result, 0, abs_tol = 1000), ("not nearing to 0", result)


def test_return_False_if_q2_notdefined():
    q1 = Qualean(0)
    assert not (bool(q1) and q2)


def test_return_True_if_q2_notdefined():
    q1 = Qualean(1)
    assert  (bool(q1) or q2)


