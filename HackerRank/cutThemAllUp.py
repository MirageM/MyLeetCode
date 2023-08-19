"""
An automated cutting machine is used to cut rods into segments. The cutting machine can only hold a rod of minLength or more. A rod is marked with the necessary cuts and their lengths are given as an array in the order they are marked. Determine if it is possible to plan the cuts so the last cut is from a rod at least minLength units long.
Example
n = 3
lengths = [4, 3, 2]
minLength = 7
The rod is initially sum(lengths) = 4 + 3 + 2 = 9 units long. First
cut off the segment of length 4 + 3 = 7 leaving a rod 9 - 7 = 2.
Then check that the length 7 rod can be cut into segments of lengths 4 and 3. Since 7 is greater than or equal to minLength = 7, the final cut can be made. Return "Possible".
Example n =3
lengths = [4, 2, 3]
minLength = 7
The rod is initially sum(lengths) = 4 + 2 + 3 = 9 units long. In
this case, the initial cut can be of length 4 or 4 + 2 = 6.
Regardless of the length of the first cut, the remaining piece
will be shorter than minLength. Because n - 1 = 2 cuts cannot
be made, the answer is "Impossible."
Function Description
Complete the function cutThemAll in the editor below.
cutThemAll has the following parameter(s):
int lengths[n]: the lengths of the segments, in order int minLength: the minimum length the machine can accept


Example n=3
lengths = [4, 2, 3]
minLength = 7
The rod is initially sum(lengths) = 4 + 2 + 3 = 9 units long. In
this case, the initial cut can be of length 4 or 4 + 2 = 6.
Regardless of the length of the first cut, the remaining piece
will be shorter than minLength. Because n - 1 = 2 cuts cannot
be made, the answer is "Impossible."
Function Description
Complete the function cutThemAll in the editor below.
cutThemAll has the following parameters):
int lengths[n]: the lengths of the segments, in order int minLength: the minimum length the machine can accept
Returns
string: "Possible" if all n-1 cuts can be made. Otherwise, return the string "Impossible"
Constraints
• 2< n<105
• 1<t<109
• 1 5 lengthslit < 109
• The sum of the elements of lengths equals the uncut rod length.


Sample Input For Custom Testing
STDIN
Function
4
3
5
4
3
9
lengths [] size n = 4
lengths [] = [3, 5, 4, 3]
minLength= 9

Sample Output
Possible

"""


def cutThemAll(lengths, minLength):
    total = sum(lengths)
    if total < minLength:
        return "Impossible"
    else:
        return "Possible"
    

def cutThemAll(lengths, minLength):
    # Input 3, 5, 6, 2, 12 Output: Impossible
    total = sum(lengths)
    if total < minLength:
        return "Impossible"
    elif total == minLength:
        return "Impossible"
    elif total > minLength:
        return "Impossible"
    elif total > minLength:
        return "Possible"
    else:
        return "Possible"

    
    
    
