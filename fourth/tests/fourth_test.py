from fourth.fourth import calculator, read_yaml
import pytest
from contextlib import nullcontext
import yaml

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
    "input_x, input_y, input_operation, exception, output",
    [
        (1, 0, "addition", nullcontext(), 1),
        (1, 0, "subtraction", nullcontext(), 1),
        (1, 0, "multiplication", nullcontext(), 0),
        (1, 0, "division", pytest.raises(ZeroDivisionError), None),
        (1, 0, "flipping", pytest.raises(ValueError), None),
        ("x", 0, "addition", pytest.raises(TypeError), None),
        (1, "y", "addition", pytest.raises(TypeError), None)
    ]
)
def test_calculator(input_x, input_y, input_operation, exception, output):
    with exception:
        assert calculator(input_x, input_y, input_operation) == output

yml_path = "/workspaces/25-06_bioinfo_ws_unit_testing/.github/workflows/main.yml"

@pytest.mark.parametrize(
    "input_filepath, exception, output",
    [
        (yml_path, nullcontext(), yaml.safe_load(open(yml_path))),
        (12, pytest.raises(ValueError), None)
    ]
)
def test_read_yaml(input_filepath, exception, output):
    with exception:
        assert read_yaml(input_filepath) == output