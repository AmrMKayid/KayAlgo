def BinarySearch_Recursive(arr, left, right, value):
	''' implemntation of Binary Search Algorithm'''
	if right >= left:
		mid = left + (right - left) // 2
		if (value == arr[mid]):
			return "Value {} found @ index {}".format(value, mid)
		elif(value < arr[mid]):
			return BinarySearch_Recursive(arr, left, mid - 1, value)
		elif(value > arr[mid]):
			return BinarySearch_Recursive(arr, mid + 1, right, value)
	else:
		return "Value does not exist on this array"


def BinarySearch_Iterative(arr, value):
	left = 0
	right = len(arr) - 1
	while right >= left:
	    mid = (right + left)//2
	    if(arr[mid] == value):
	        return "Value {} found @ index {}".format(value, mid)
	    elif(arr[mid] > value):
	        right = mid - 1
	    elif(arr[mid] < value):
	        left = mid + 1
	return "Value does not exist on this array"

def main():
	arr = [0, 1, 2, 3, 4, 5, 6, 7]
	print("BinarySearch Recursive")
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, -1))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 6))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 3))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 0))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 5))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 7))
	print(BinarySearch_Recursive(arr, 0, len(arr) - 1, 8))

	print("\nBinarySearch Iterative")
	print(BinarySearch_Iterative(arr, -1))
	print(BinarySearch_Iterative(arr, 6))
	print(BinarySearch_Iterative(arr, 3))
	print(BinarySearch_Iterative(arr, 0))
	print(BinarySearch_Iterative(arr, 5))
	print(BinarySearch_Iterative(arr, 7))
	print(BinarySearch_Iterative(arr, 8))



if __name__ == '__main__':
	main()

