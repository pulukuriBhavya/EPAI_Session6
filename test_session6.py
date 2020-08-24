import pytest
import inspect
#from test_utils import *
import re
import os.path
import sys

import session6



def test_fourspace():
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


FUNCTION_CHECK_FOR = [
    'create_cards_lambda',
    'create_cards',
    'cards_eval',
    'cards_conversion',
    'poker'
]


def test_functions_avaiable():
    FUNCTIONSAVAILABLE = True
    f = open("session6.py", "r")
    content = f.read()
    f.close()
    for c in FUNCTION_CHECK_FOR:
        if c not in content:
            FUNCTIONSAVAILABLE = False
            pass
    assert FUNCTIONSAVAILABLE == True, "You have not implemented all the functions"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"



def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

