import pytest
import inspect
#from test_utils import *
import re
import os.path
import sys

import session6

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck= [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]

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

README_CONTENT_CHECK_FOR = [
    'create_cards_lambda',
    'create_cards',
    'cards_eval',
    'cards_conversion',
    'poker',
    'player',
    'winner'
]

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

def test_lamda_manual_check():
    r = sorted(session6.create_cards_lambda(vals, suits))
    assert r == sorted(deck), "Your Lambda function does not return proper deck of cards"

def test_create_cards_manual_check():
    r = sorted(session6.create_cards(vals, suits))
    assert r == sorted(deck), "Your function does not return proper deck of cards"

def test_annotations_poker_check():
    r = session6.poker()
    assert len(session6.poker.__annotations__) > 0, f'Annotations not present for your function'

def test_docstring_poker_check():
    r = session6.poker()
    assert len(session6.poker.__doc__) > 0, f'Docstring not present for your function'

def test_docstring_create_cards_check():
    r = session6.create_cards(vals, suits)
    assert len(r.__doc__) > 0, f'Docstring not present for your function'

def test_random_tests_20_check():
    player1 = [[('queen', 'hearts'), ('queen', 'diamonds'), ('2', 'diamonds')],
               [('7', 'spades'), ('8', 'spades'), ('3', 'diamonds')],
               [('7', 'clubs'), ('ace', 'clubs'), ('queen', 'diamonds')],
               [('6', 'diamonds'), ('3', 'spades'), ('5', 'diamonds'), ('10', 'diamonds')],
               [('6', 'clubs'), ('ace', 'diamonds'), ('8', 'diamonds')],
               [('7', 'hearts'), ('queen', 'diamonds'), ('5', 'clubs'), ('queen', 'clubs'), ('jack', 'spades')],
               [('6', 'clubs'), ('queen', 'diamonds'), ('7', 'hearts')],
               [('9', 'diamonds'), ('10', 'hearts'), ('3', 'clubs')],
               [('6', 'diamonds'), ('6', 'diamonds'), ('9', 'hearts'), ('7', 'hearts'), ('10', 'diamonds')],
               [('4', 'clubs'), ('queen', 'diamonds'), ('queen', 'hearts')],
               [('2', 'clubs'), ('8', 'diamonds'), ('queen', 'hearts')],
               [('9', 'clubs'), ('queen', 'hearts'), ('9', 'diamonds'), ('10', 'diamonds')],
               [('8', 'clubs'), ('9', 'spades'), ('7', 'diamonds')],
               [('3', 'clubs'), ('queen', 'spades'), ('2', 'spades'), ('9', 'hearts')],
               [('10', 'hearts'), ('10', 'hearts'), ('queen', 'clubs'), ('jack', 'diamonds'), ('4', 'hearts')],
               [('5', 'spades'), ('4', 'clubs'), ('10', 'diamonds'), ('3', 'diamonds')],
               [('5', 'clubs'), ('2', 'clubs'), ('10', 'spades'), ('6', 'spades'), ('jack', 'clubs')],
               [('5', 'hearts'), ('7', 'clubs'), ('10', 'diamonds'), ('4', 'clubs')],
               [('ace', 'diamonds'), ('6', 'hearts'), ('2', 'hearts'), ('ace', 'hearts'), ('9', 'spades')],
               [('3', 'hearts'), ('4', 'spades'), ('ace', 'clubs')]]
    #for i in range(len(player1)):
    #    p1 = player1[i]
    #    print("p1 after for")
    #    print(p1)
    player2 = [[('jack', 'diamonds'), ('ace', 'spades'), ('king', 'clubs')],
               [('3', 'diamonds'), ('9', 'diamonds'), ('10', 'hearts')],
               [('ace', 'hearts'), ('8', 'hearts'), ('ace', 'hearts')],
               [('3', 'diamonds'), ('7', 'spades'), ('ace', 'clubs'), ('queen', 'hearts')],
               [('10', 'spades'), ('jack', 'hearts'), ('jack', 'spades')],
               [('queen', 'hearts'), ('2', 'spades'), ('10', 'spades'), ('3', 'diamonds'), ('king', 'clubs')],
               [('8', 'spades'), ('3', 'hearts'), ('9', 'clubs')],
               [('queen', 'spades'), ('queen', 'spades'), ('jack', 'diamonds')],
               [('4', 'hearts'), ('9', 'hearts'), ('8', 'hearts'), ('5', 'clubs'), ('8', 'diamonds')],
               [('3', 'diamonds'), ('9', 'hearts'), ('9', 'diamonds')],
               [('9', 'spades'), ('queen', 'hearts'), ('4', 'clubs')],
               [('9', 'hearts'), ('9', 'clubs'), ('2', 'spades'), ('jack', 'spades')],
               [('6', 'diamonds'), ('5', 'clubs'), ('ace', 'clubs')],
               [('3', 'diamonds'), ('5', 'clubs'), ('9', 'diamonds'), ('9', 'clubs')],
               [('jack', 'hearts'), ('queen', 'clubs'), ('king', 'diamonds'), ('6', 'diamonds'), ('jack', 'clubs')],
               [('5', 'hearts'), ('10', 'spades'), ('3', 'hearts'), ('3', 'clubs')],
               [('7', 'diamonds'), ('3', 'hearts'), ('10', 'hearts'), ('9', 'hearts'), ('2', 'clubs')],
               [('ace', 'spades'), ('5', 'diamonds'), ('ace', 'clubs'), ('2', 'hearts')],
               [('2', 'hearts'), ('6', 'hearts'), ('7', 'clubs'), ('jack', 'diamonds'), ('6', 'clubs')],
               [('9', 'clubs'), ('2', 'clubs'), ('6', 'spades')]]
    #for i in range(len(player2)):
    #    p2 = player2[i]
    #    print("p2 after for")
    #    print(p2)
    result = ['Player1 wins', 'No one Win', 'Player2 wins', 'No one Win', 'Player2 wins',
              'Player1 wins', 'No one Win', 'Player2 wins', 'Player2 wins', 'Player1 wins',
              'No one Win', 'Player2 wins', 'Player1 wins', 'Player2 wins', 'Player2 wins',
              'Player2 wins', 'No one Win', 'Player2 wins', 'Player1 wins', 'No one Win']
    for i in range(len(player1)):
        #print("p1 inside for range" )
        #print("p2 inside for range" )
        p1 = player1[i]
        p2 = player2[i]
        r = session6.poker(p1,p2)
        assert r == result[i], "Your function is not working properly"

def test_3_card_set():
    p1 = [('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs')]
    p2 = [('9', 'spades'), ('queen', 'hearts'), ('4', 'clubs')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for 3 set of cards"

def test_4_card_set():
    p1 = [('9', 'diamonds'), ('8', 'diamonds'), ('7', 'diamonds'), ('10', 'diamonds')]
    p2 = [('6', 'diamonds'), ('3', 'spades'), ('5', 'diamonds'), ('10', 'diamonds')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for 4 set of cards"

def test_5_card_set():
    p1 = [('8', 'hearts'), ('6', 'diamonds'), ('7', 'clubs'), ('5', 'spades'),('4','hearts')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for 5 set of cards"

def test_royal_flush():
    p1 = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts'),('10','hearts')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for Royal Flush"

def test_straight_flush():
    p1 = [('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs'),('10','clubs')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for straight Flush"

def test_four_of_a_kind():
    p1 = [('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'spades'), ('queen', 'diamonds'),('5','clubs')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for four of a kind"

def test_full_house():
    p1 = [('ace', 'hearts'), ('ace', 'spades'), ('ace', 'diamonds'), ('king', 'spades'),('king','hearts')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for full house"

def test_flush():
    p1 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts'), ('4', 'hearts'),('2','hearts')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for Flush"

def test_straight():
    p1 = [('5', 'spades'), ('8', 'hearts'), ('7', 'clubs'), ('6', 'diamonds'),('4','hearts')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for straight"

def test_three_of_a_kind():
    p1 = [('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('7', 'hearts'),('2','clubs')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for three of a kind"

def test_two_pair():
    p1 = [('jack', 'diamonds'), ('jack', 'spades'), ('9', 'spades'), ('9', 'diamonds'),('5','clubs')]
    p2 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for two pair"

def test_one_pair():
    p1 = [('king', 'spades'), ('king', 'hearts'), ('9', 'diamonds'), ('8', 'spades'),('4','hearts')]
    p2 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'),('2','diamonds')]
    r = session6.poker(p1,p2)
    assert r == "Player1 wins", "Your function is not working properly for one pair"