# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_position_of_element(array, target, is_first_element: bool = False) -> int:
    array_size = len(array)
    left = 0
    right = array_size - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid, is_first_element)
        print(array[mid])
        if array[mid] == target:
            if is_first_element:
                if mid == 0 or (array[mid - 1] != target and mid - 1 >= 0):
                    print('mid value:', mid)
                    return mid
                right = mid - 1
            else:
                if mid == array_size - 1 or (
                        array[mid + 1] != target and (mid + 1 < array_size - 1)):
                    return mid
                left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search_range(array: List[int], target: int) -> List[int]:
    first = get_position_of_element(array, target, True)
    last = get_position_of_element(array, target)
    return [first, last]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(search_range([10, 10, 11, 11, 11, 11, 13, 14, 15], 11))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
