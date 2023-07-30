# Dominating XOR
'''
For an arry arr of n positive integers, count the unordered
pairs (i, j) (0 <= i < j < n) where arr[i] XOR arr[j] > arr[i] AND
arr[j]. XOR denotes the bitwise XOR operation and AND
denotes the bitwise AND operation.
'''
def dominatingXorPairs(arr):
	result = 0
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] ^ arr[j] > arr[i] & arr[j]:
				result += 1
	return result


def dominatingXorPairs(arr):
	result = 0
	for i in range(len(arr)):
		j = i + 1
		if arr[i] ^ arr[j] > arr[i] & arr[j]:
			result += 1
	return result