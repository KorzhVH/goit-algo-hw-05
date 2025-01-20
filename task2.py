#NOTE!!
#Something in binar_search logic breaks sometimes, I can't figure out why. It woks 50/50


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
    # insuring that target within range of array
    if target < array[low] or target > array[high]:
        return "Target not in range"
    counter = 0
    while low <= high and low <= target <= high:
        counter+=1
        mid = (low + high) // 2

        if array[mid] < target <= array[mid+1]:
            print(f'{counter}:{array[mid+1]}')
            return {counter:array[mid+1]}
        elif array[mid-1] < target < array[mid]:
            print(f'{counter}:{array[mid]}')
            return {counter: array[mid]}
        elif target > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

if __name__ == "__main__":
    binar_search(generate_sorted_array(), 7)