def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i > -1 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    print(a)


insertion_sort([3, 4, 7, 1, 0, 6, 2, 5])
