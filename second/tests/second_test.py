from second.second import greeting

def test_greeting_eng():
    assert greeting("James", "English") == "Hello James!"

def test_greeting_nor():
    assert greeting("Solveig", "Norwegian") == "Hei Solveig!"

def test_greeting_default():
    assert greeting("Max", "German") == "I don't speak your language!"



import pytest
def test_add_exception():
    with pytest.raises(TypeError):
        assert greeting(5,"English") == "I don't speak your language!"
# add unit tests to cover exceptions in greeting(name, language) in second/second.py
# start by importing pytest: import pytest
# in your new test function include: with pytest.raises(<exception name>):
# continue by using assert
# add your changes: git add second/tests/second_test.py
# commit your changes using commit message conventions (https://inpred.github.io/24-03_bioinfo_ws/#19): git commit -m "test: <your commit message>"