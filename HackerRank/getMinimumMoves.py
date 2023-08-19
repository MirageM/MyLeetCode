'''
There are n types of items in a shop's inventory, where the
quanittiy of the ithth item is denoted by quantity[i]. These items
are to be shipped in two consignments, where the first
consignment contains items of type [1, 2, .., j], and the second
consignment contains the reminaing item types, where j can
be chosen such that 1<= j < n.. Note that both conisgnments must be non-empty,
and all items of a type must be in the same consignment.

The shopkeeper wants the item counts in each cosignment to be equal.
To achieve this, the shopkeeper can perform the following move 
any number of times: increase or decrease the quanity of any item type
by 1. The quantity of each item type must remain positive throughout.

Find the minimum number of moves in which the total quanities of both 
consignments can be equal if the item types are split optimally.



 # Write your code here
    # Input: 5 3 3 6 3 9 Output: 0
    # Input: 3 4 5 7 Output: 2
    # input: 3 1 4 4 Output: 1
'''




import math
import os
import random
import re
import sys



def getMinimumMoves(quantity):





#
# Complete the 'getMinimumMoves' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY quantity as parameter.
#
