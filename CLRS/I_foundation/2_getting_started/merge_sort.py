def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
    return arr


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = arr[p + i - 1]
    for j in range(n2):
        right[j] = arr[q + j]
    left[n1] = float('Inf')
    right[n2] = float('Inf')
    i = j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    arr = merge_sort(arr, 0, len(arr))
    print(arr)
