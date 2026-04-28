import json
from solution import solution

def test_solution():
    with open("test_cases.json") as f:
        cases = json.load(f)

    for case in cases:
        result = solution(**case["input"])
        assert result == case["output"]
