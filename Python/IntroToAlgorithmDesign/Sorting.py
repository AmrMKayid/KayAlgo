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


print(insertion_sort([154, 245, 568, 324, 654, 324]))

print(insertion_sort(["Mike", "Bob", "Sally", "Jill", "Jan"]))