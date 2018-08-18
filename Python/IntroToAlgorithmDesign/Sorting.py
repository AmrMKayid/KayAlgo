def insertion_sort(arr):
    """
    insertion sort is a method for sorting that starts with a single element (thus forming a trivially sorted list)
    and then incrementally inserts the remaining elements so that the list stays sorted
    :param arr: array that need to be sorted
    :return: sorted array
    """
    for i in range(1, len(arr)):
        j = i
        while (j > 0) and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


def selection_sort(arr):
    """
    selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
    :param arr: array that need to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print("#----------- Insertion Sort -----------#")

print(insertion_sort([154, 245, 568, 324, 654, 324]))

print(insertion_sort(["Mike", "Bob", "Sally", "Jill", "Jan"]))

print("\n\n")

print("#----------- Selection Sort -----------#")

print(selection_sort([154, 245, 568, 324, 654, 324]))

print(selection_sort(["Mike", "Bob", "Sally", "Jill", "Jan"]))
