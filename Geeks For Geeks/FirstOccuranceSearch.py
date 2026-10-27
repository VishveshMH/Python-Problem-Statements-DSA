def first(arr, low, high, x, n):
	if(high >= low):
		mid = low + (high - low) // 2
		if((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
			return mid
		elif(x > arr[mid]):
			return first(arr, (mid + 1), high, x, n)
		else:
			return first(arr, low, (mid - 1), x, n)

	return -1

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
ret = first(arr, n, x)
print(ret)
