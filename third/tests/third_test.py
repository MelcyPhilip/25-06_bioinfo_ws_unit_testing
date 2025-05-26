from third.third import greeting
import pytest
from contextlib import nullcontext

# write one unit test to cover all test cases of greeting(name, language) in third/third.py
# also import nullcontext: from contextlib import nullcontext
# add parametrize decorator as header to your test function: @pytest.mark.parametrize()
# define variables for input, exception and output as a string: "input, exception, output"
# create list containing tuples with test cases
# each tuple is a test case: ("<name>", "<language>", <exception or nullcontext>, <excepted output>)
# remove the old test after you have completed the task
# add your changes: git add third/tests/third_test.py
# commit your changes using commit message conventions (https://inpred.github.io/24-03_bioinfo_ws/#19): git commit -m "test: <your commit message>"

@pytest.mark.parametrize(
    "input_name, input_language, exception, output",
    [
        ("James", "English", nullcontext(), "Hello James!"),
        ("Solveig", "Norwegian", nullcontext(), "Hei Solveig!"),
        ("Max", "German", nullcontext(), "I don't speak your language!"),
        (False, "English", pytest.raises(TypeError), None),
        ("James", 666, pytest.raises(TypeError), None)
    ]
)
def test_greeting(input_name, input_language, exception, output):
    with exception:
        assert greeting(input_name, input_language) == output