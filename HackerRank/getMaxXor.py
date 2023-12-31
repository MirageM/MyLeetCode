# https://www.hackerrank.com/challenges/maximizing-xor/problem
# Maximizing XOR
# Time Complexity: O(1) Space Complexity: O(1)
def getMaxXor(n):
	num_bits = len(bin(n)) - 2
	max_xor = (1 << num_bits) - 1
	return max_xor - 1


def getMaxXor(n):
	num_bits = len(bin(n)) - 2
	max_xor = (1 << num_bits) - 1
	return max_xor - 1