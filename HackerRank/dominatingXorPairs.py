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