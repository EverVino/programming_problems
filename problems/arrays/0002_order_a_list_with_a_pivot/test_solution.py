import json
from solution import solution

def test_solution():
    with open("test_cases.json") as f:
        cases = json.load(f)

    for case in cases:
        index = case["input"]["index"]
        array = case["input"]["array"]
        pivot = array[index]
        result = solution(index, array)
        print("pivot", pivot)
        i = 0
        while i < len(result):
            if result[i] > pivot:
                break
            i += 1
        while i < len(result):
            if result[i] <= pivot:
                raise Exception("wrong result")
            i += 1

    print("All test passed")

test_solution()
