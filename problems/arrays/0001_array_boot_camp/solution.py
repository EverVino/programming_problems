def solution(array):
    left_even, right_odd = 0, len(array) - 1

    while left_even < right_odd:
        if array[left_even] % 2 == 0:
            left_even += 1
        else:
            array[left_even], array[right_odd] = array[right_odd], array[left_even]
            right_odd -= 1
    return array

