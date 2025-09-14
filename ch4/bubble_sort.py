def bubble_sort(array):
    unsorted_until_index = len(array) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        unsorted_until_index -= 1

    return array

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([1, 2, 3, 4, 5, 6]))
print(bubble_sort([6, 5, 4, 3, 2, 1]))
print(bubble_sort([1, 2, 3, 4, 5, 6, 7]))
print(bubble_sort([7, 6, 5, 4, 3, 2, 1]))
