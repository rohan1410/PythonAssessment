def func(x):
	return x[-1]  #Last element of tuple

if __name__ == '__main__':
	arr = raw_input().split() #Taking input a list of tuples
	arr = sorted(arr,key = func)  #Sorting arr using defined function func in increasing order
	print arr #printing array
