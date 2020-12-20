import pytest
import session9
import os
import inspect
import re
from freezegun import freeze_time
from session9 import *

README_CONTENT_CHECK_FOR = [
    'decorator',
    'odd',
    'log',
    'authenticate',
    'time',
    'privilege',
    'Single Dispatch'
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
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  



def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



@freeze_time("2020-10-04 19:18:28")
def test_odd_run_even():
    @odd_run
    def add(a: int, b: int) -> int:
        return a + b
    assert add(1, 2) == None



@freeze_time("2020-10-04 19:18:51")
def test_odd_run_odd():
    @odd_run
    def add(a: int, b: int) -> int:
        return a + b
    assert add(1, 2) == 3


@authenticate(current_password = "TSAI@Welcome", user_password = 'TSAI@Welcome')
def add(a: int, b: int) -> int:
    return (a + b)



@authenticate(current_password = "TSAI@Welcome", user_password = 'Python@2020')
def mul(a: int, b: int) -> int:
    return (a * b)



def test_authenticate_decorator_correct_password():
    assert add(1, 2) == 3, "Something wrong with authentication."



def test_authenticate_decorator_incorrect_password():
    assert mul(1, 2) == None, "Something wrong with authentication."



@privilegeDecorator("high")
def dummy_h(**kwargs):
    return sum(list(kwargs.values()))



@privilegeDecorator("mid")
def dummy_m(**kwargs):
    return sum(list(kwargs.values()))



@privilegeDecorator("low")
def dummy_l(**kwargs):
    return sum(list(kwargs.values()))



@privilegeDecorator("no")
def dummy_n(**kwargs):
    return sum(list(kwargs.values()))



def test_privilegeDecorator():
    _ = dummy_h(a = 10, b = 20, c = 30, d = 40)
    assert _ == 100, "Access privilege logic failed!"
    _ = dummy_m(a = 10, b = 20, c = 30, d = 40)
    assert _ == 60, "Access privilege logic failed!"
    _ = dummy_l(a = 10, b = 20, c = 30, d = 40)
    assert _ == 30, "Access privilege logic failed!"
    _ = dummy_n(a = 10, b = 20, c = 30, d = 40)
    assert _ == 10, "Access privilege logic failed!"



def test_singledispatch():
    assert htmlize(106) == '106(<i>0x6a</i>)'

    assert htmlize({'a': 10, 'b': 20, 'c': 30}) == """<ul>
<li>a=10</li>
<li>b=20</li>
<li>c=30</li>
</ul>"""

    assert htmlize([1, 2, 3, 4]) == """<ul>
<li>1(<i>0x1</i>)</li>
<li>2(<i>0x2</i>)</li>
<li>3(<i>0x3</i>)</li>
<li>4(<i>0x4</i>)</li>
</ul>"""

    assert htmlize(((1, 10), (2, 20), (3, 30))) == """<ul>
<li><ul>
<li>1(<i>0x1</i>)</li>
<li>10(<i>0xa</i>)</li>
</ul></li>
<li><ul>
<li>2(<i>0x2</i>)</li>
<li>20(<i>0x14</i>)</li>
</ul></li>
<li><ul>
<li>3(<i>0x3</i>)</li>
<li>30(<i>0x1e</i>)</li>
</ul></li>
</ul>"""

    assert htmlize('1000 < 10000') == '1000 &lt; 10000'

    assert htmlize('Test String\n') == 'Test String<br/>\n'

    assert htmlize(3.1417) == '(<i>3.14</i>)'