import json
from solution import solution

def check_valid_array(result):
    i = 0
    while i < len(result): 
        if result[i] % 2 == 0:
            i += 1
        else:
            break
    while i < len(result):
        if result[i] % 2 != 0:
            i += 1
        else:
            return False

    return True

def test_solution():
    with open("test_cases.json") as f:
        cases = json.load(f)

    for case in cases:
        result = solution(case["input"])
        assert(check_valid_array(result))
    print("All test passed")

if __name__ == "__main__":
    test_solution()
