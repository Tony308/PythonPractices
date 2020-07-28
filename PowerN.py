import math
def index(array, n):
	length = len(array)
	if n > length-1:
		return -1
	return math.pow(array[n],n)