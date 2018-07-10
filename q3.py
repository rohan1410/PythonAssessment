def binarySearch (arr, l, r, x):
    if r >= l:
 
        mid = l + (r - l)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:

        return -1

if __name__ == '__main__':
	arr = raw_input().split() # Input sorted element array
	x = raw_input() #element to be found
	res = binarySearch(arr, 0, len(arr) - 1, x)
	if  res == -1: # If element not found 
		print 'Element not Found'
	else:
		print res 
