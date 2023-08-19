"""
Consider two arrays of integers, a[n] and b[n]. What is the maximum number of pairs that can be formed where a[i]> b[j]? Each element can be in no more than one pair.
Find the maximum number of such possible pairs.
Example n=3
a = [1, 2, 3]
b = [1, 2, 1]
Two ways the maximum number of pairs can be selected:
• {a[1], b[0])=42, 1} and {a[2], b[21)={3, 1} are valid pairs.
• fa[1], b[0])=42, 1} and fa[2], b[1])={3, 2} are valid pairs.
No more than 2 pairs can be formed, so return 2.
Function Description
Complete the function findNumOfPairs in the editor below.
findNumOfPairs has the following parameters:
int a[n]: an array of integers int b[n]: an array of integers
Returns
int: the maximum number of pairs possible
Constraints
• 1 5n5105
• 1 sails 10°
• 1s blils 10°
• Input Format For Custom Testing

"""

def findNumOfPairs(a, b):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] > b[j]:
                count += 1
    return count