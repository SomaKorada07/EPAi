import pytest
import session6
import os
import inspect
import re

README_CONTENT_CHECK_FOR = [
    'lambda',
    'zip',
    'map',
    'suits',
    'vals',
    'deck',
    'poker',
    'rank'
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
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"  


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_annotations():
    set1 = {('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}
    assert len(session6.determine_rank.__annotations__) > 0, f'annotations are not written'


def test_docstrings():
    set1 = {('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}
    assert len(session6.determine_rank.__doc__) > 0, f'docstrings are not written'


def test_len_lambda_deck():
    assert len(session6.lambda_deck()) == 52, f'Lambda function is incorrect'


def test_len_func_deck():
    assert len(session6.prepare_deck()) == 52, f'Simple function to prepare deck is incorrect'


def test_empty_set():
    set1 = {}
    set2 = {('5', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')}
    with pytest.raises(ValueError):
        session6.determine_winner(set1, set2)


def test_unequal_set():
    set1 = {('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}
    set2 = {('5', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')}
    with pytest.raises(ValueError):
        session6.determine_winner(set1, set2)


def test_same_card():
    set1 = {('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}
    set2 = {('5', 'hearts'), ('queen', 'clubs'), ('6', 'clubs')}
    with pytest.raises(ValueError):
        session6.determine_winner(set1, set2)


def test_card_count():
    set1 = {('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}
    set2 = {('5', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds'), ('8', 'clubs')}
    with pytest.raises(ValueError):
        session6.determine_winner(set1, set2)


def test_winner_three_cards():
    set1 = {('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')} #1

    set2 = {('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs')} #2

    set3 = {('queen', 'spades'), ('queen', 'clubs'), ('6', 'clubs')} #3

    set4 = {('ace', 'spades'), ('ace', 'hearts'), ('king', 'hearts')} #3

    set5 = {('king', 'hearts'), ('5', 'hearts'), ('6', 'hearts')} #5

    set6 = {('8', 'hearts'), ('7', 'clubs'), ('6', 'diamonds')} #6

    set7 = {('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds')} #7

    set8 = {('jack', 'diamonds'), ('jack', 'hearts'), ('9', 'spades')} #3

    set9 = {('king', 'hearts'), ('king', 'spades'), ('9', 'diamonds')} #3

    set10 = {('ace', 'diamonds'), ('queen', 'clubs'), ('6', 'hearts')} #10

    assert session6.determine_winner(set1, set2) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set2, set3) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set3, set4) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set6, set5) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set7, set8) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set8, set9) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set9, set10) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set1, set10) == "player1", f'Logic is incorrect'


def test_winner_four_cards():
    set1 = {('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')} #1

    set2 = {('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs')} #2

    set3 = {('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('6', 'clubs')} #3

    set4 = {('ace', 'spades'), ('ace', 'hearts'), ('king', 'spades'), ('king', 'hearts')} #4

    set5 = {('king', 'hearts'), ('2', 'hearts'), ('6', 'hearts'), ('4', 'hearts')} #5

    set6 = {('8', 'hearts'), ('7', 'clubs'), ('6', 'diamonds'), ('5', 'spades')} #6

    set7 = {('queen', 'clubs'), ('queen', 'hearts'), ('7', 'hearts'), ('2', 'spades')} #7

    set8 = {('jack', 'diamonds'), ('jack', 'hearts'), ('9', 'spades'), ('9', 'diamonds')} #4

    set9 = {('king', 'hearts'), ('king', 'spades'), ('4', 'diamonds'), ('8', 'spades')} #7

    set10 = {('ace', 'diamonds'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades')} #10

    assert session6.determine_winner(set1, set2) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set2, set3) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set3, set4) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set6, set5) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set7, set8) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set8, set9) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set9, set10) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set1, set10) == "player1", f'Logic is incorrect'



def test_winner_five_cards():
    set1 = {('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts'), ('10', 'hearts')}

    set2 = {('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}

    set3 = {('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('2', 'clubs')}

    set4 = {('ace', 'spades'), ('ace', 'hearts'), ('ace', 'diamonds'), ('king', 'spades'), ('king', 'hearts')}

    set5 = {('king', 'hearts'), ('3', 'hearts'), ('6', 'hearts'), ('9', 'hearts'), ('2', 'hearts')}

    set6 = {('8', 'hearts'), ('7', 'clubs'), ('6', 'diamonds'), ('5', 'spades'), ('4', 'hearts')}

    set7 = {('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('7', 'hearts'), ('2', 'spades')}

    set8 = {('jack', 'diamonds'), ('jack', 'hearts'), ('9', 'spades'), ('9', 'diamonds'), ('5', 'clubs')}

    set9 = {('king', 'hearts'), ('king', 'spades'), ('9', 'clubs'), ('8', 'spades'), ('4', 'hearts')}

    set10 = {('ace', 'diamonds'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')}

    assert session6.determine_winner(set1, set2) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set2, set3) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set3, set4) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set6, set5) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set8, set7) == "player2", f'Logic is incorrect'
    assert session6.determine_winner(set8, set9) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set9, set10) == "player1", f'Logic is incorrect'
    assert session6.determine_winner(set1, set10) == "player1", f'Logic is incorrect'


def test_rank_royal_flush():
    set1 = {('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts'), ('10', 'hearts')}

    assert session6.determine_rank(set1) == 1, f'Logic is incorrect'


def test_rank_straight_flush():
    set1 = {('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('7', 'clubs'), ('6', 'clubs')}

    assert session6.determine_rank(set1) == 2, f'Logic is incorrect'


def test_rank_four_of_a_kind():
    set1 = {('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('2', 'clubs')}

    assert session6.determine_rank(set1) == 3, f'Logic is incorrect'


def test_rank_full_house():
    set1 = {('ace', 'spades'), ('ace', 'hearts'), ('ace', 'diamonds'), ('king', 'spades'), ('king', 'hearts')}

    assert session6.determine_rank(set1) == 4, f'Logic is incorrect'


def test_rank_flush():
    set1 = {('king', 'hearts'), ('3', 'hearts'), ('6', 'hearts'), ('9', 'hearts'), ('2', 'hearts')}

    assert session6.determine_rank(set1) == 5, f'Logic is incorrect'


def test_rank_straight():
    set1 = {('8', 'hearts'), ('7', 'clubs'), ('6', 'diamonds'), ('5', 'spades'), ('4', 'hearts')}

    assert session6.determine_rank(set1) == 6, f'Logic is incorrect'


def test_rank_three_of_a_kind():
    set1 = {('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('7', 'hearts'), ('2', 'spades')}

    assert session6.determine_rank(set1) == 7, f'Logic is incorrect'


def test_rank_two_pair():
    set1 = {('jack', 'diamonds'), ('jack', 'hearts'), ('9', 'spades'), ('9', 'diamonds'), ('5', 'clubs')}

    assert session6.determine_rank(set1) == 8, f'Logic is incorrect'


def test_rank_one_pair():
    set1 = {('king', 'hearts'), ('king', 'spades'), ('9', 'clubs'), ('8', 'spades'), ('4', 'hearts')}

    assert session6.determine_rank(set1) == 9, f'Logic is incorrect'


def test_rank_high_card():
    set1 = {('ace', 'diamonds'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')}

    assert session6.determine_rank(set1) == 10, f'Logic is incorrect'






