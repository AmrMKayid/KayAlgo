def BinarySearch(arr, left, right, value):
	''' implemntation of Binary Search Algorithm'''
	if right >= left:
		mid = left + (right - left) // 2
		if (value == arr[mid]):
			return "Value {} found @ index {}".format(value, mid)
		elif(value < arr[mid]):
			return BinarySearch(arr, left, mid - 1, value)
		elif(value > arr[mid]):
			return BinarySearch(arr, mid + 1, right, value)
	else:
		return "Value does not exist on this array"


def main():
	arr = [0, 1, 2, 3, 4, 5, 6, 7]
	print(BinarySearch(arr, 0, len(arr) - 1, -1))
	print(BinarySearch(arr, 0, len(arr) - 1, 6))
	print(BinarySearch(arr, 0, len(arr) - 1, 3))
	print(BinarySearch(arr, 0, len(arr) - 1, 0))
	print(BinarySearch(arr, 0, len(arr) - 1, 5))
	print(BinarySearch(arr, 0, len(arr) - 1, 7))
	print(BinarySearch(arr, 0, len(arr) - 1, 8))



if __name__ == '__main__':
	main()

