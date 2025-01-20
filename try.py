#Something in binar

import random

#used for sorting randomly generated floats from generate_sorted_array(),
#sort() returns None
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# created array of 100 floats, then sorts it with insertion_sort()
def generate_sorted_array():
    arr = [random.uniform(0, 100) for _ in range(0, 100)]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
    return sorted_arr


def binar_search(array, target):
    low = 0
    high = len(array) - 1

    # Ensure that the target is within the array's range
    if target < array[low] or target >= array[high]:
        return "Target not in range"

    counter = 0
    smallest = None

    while low <= high:
        counter += 1
        mid = (low + high) // 2

        if array[mid] <= target:
            low = mid + 1
        else:
            smallest = array[mid]
            high = mid - 1

    # Return the smallest float found and steps taken
    if smallest:
        print(f"{counter}:{smallest}")
        return counter, smallest
    else:
        return "No element found"


if __name__ == "__main__":
    binar_search(generate_sorted_array(), 7)