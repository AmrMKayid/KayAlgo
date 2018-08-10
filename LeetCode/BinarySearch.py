class BinarySearch():
    '''
    Read Google Blog about Binary Search BUG:
    https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

    The binary-search bug applies equally to mergesort, and to other divide-and-conquer algorithms.

    -> mid value: it fails if the sum of low and high is greater than the maximum positive int value (2^31 - 1).
    '''

    def Recursive(self, arr, left, right, value):
        ''' implemntation of Recursive Binary Search Algorithm'''
        if len(arr) == 0:
            return -1

        if right >= left:
            mid = left + ((right - left) // 2)
            if (value == arr[mid]):
                return "Value {} found @ index {}".format(value, mid)
            elif (value < arr[mid]):
                return self.Recursive(arr, left, mid - 1, value)
            elif (value > arr[mid]):
                return self.Recursive(arr, mid + 1, right, value)
        else:
            return "Value does not exist on this array"

    def Iterative(self, arr, value):
        ''' implemntation of Iterative Binary Search Algorithm'''
        if len(arr) == 0:
            return -1

        left = 0
        right = len(arr) - 1
        while right >= left:
            mid = left + ((right - left) // 2)
            if (arr[mid] == value):
                return "Value {} found @ index {}".format(value, mid)
            elif (arr[mid] > value):
                right = mid - 1
            elif (arr[mid] < value):
                left = mid + 1
        return "Value does not exist on this array"


def main():
    bs = BinarySearch()
    arr = [0, 1, 2, 3, 4, 5, 6, 7]

    print("BinarySearch Recursive")
    print(bs.Recursive(arr, 0, len(arr) - 1, -1))
    print(bs.Recursive(arr, 0, len(arr) - 1, 6))
    print(bs.Recursive(arr, 0, len(arr) - 1, 3))
    print(bs.Recursive(arr, 0, len(arr) - 1, 0))
    print(bs.Recursive(arr, 0, len(arr) - 1, 5))
    print(bs.Recursive(arr, 0, len(arr) - 1, 7))
    print(bs.Recursive(arr, 0, len(arr) - 1, 8))

    print("\nBinarySearch Iterative")
    print(bs.Iterative(arr, -1))
    print(bs.Iterative(arr, 6))
    print(bs.Iterative(arr, 3))
    print(bs.Iterative(arr, 0))
    print(bs.Iterative(arr, 5))
    print(bs.Iterative(arr, 7))
    print(bs.Iterative(arr, 8))


if __name__ == '__main__':
    main()
