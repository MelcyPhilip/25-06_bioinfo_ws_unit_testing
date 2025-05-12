from third.third import greeting
import pytest

def test_greeting_eng():
    assert greeting("James", "English") == "Hello James!"

def test_greeting_nor():
    assert greeting("Solveig", "Norwegian") == "Hei Solveig!"

def test_greeting_default():
    assert greeting("Max", "German") == "I don't speak your language!"

def test_greeting_name_wrong_type():
    with pytest.raises(TypeError):
        assert greeting(False, "English") == None

def test_greeting_language_wrong_type():
    with pytest.raises(TypeError):
        assert greeting("James", 666) == None

# write one unit test to cover all test cases of greeting(name, language) in third/third.py
# start by importing pytest: import pytest
# also import nullcontext: from contextlib import nullcontext
# add parametrize decorator as header to your test function: @pytest.mark.parametrize()
# define variables for input, exception and output as a string: "input, exception, output"
# create list containing tuples with test cases
# each tuple is a test case: ("<name>", "<language>", <exception or nullcontext>, <excepted output>)
# remove the old test after you have completed the task
# add your changes: git add third/tests/third_test.py
# commit your changes using commit message conventions (https://inpred.github.io/24-03_bioinfo_ws/#19): git commit -m "test: <your commit message>"