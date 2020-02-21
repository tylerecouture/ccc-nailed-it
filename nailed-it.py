"""
https://hackerspace.sd72.bc.ca/media/attachments/postman_message/354/nailedit.pdf

Problem J5: Nailed It!

Time limit: 2 seconds

Problem Description
Tudor is a contestant in the Canadian Carpentry Challenge (CCC). To win the CCC, 
Tudor must demonstrate his skill at nailing wood together to make the longest fence 
possible using boards. To accomplish this goal, he has N pieces of wood. The ith piece 
of wood has integer lengthLi.Aboardis made up of exactly twopieces of wood.  The 
length of a board made of wood with lengths Li and Lj is Li+Lj.  A fence consists of boards 
that are the same length.  Thelength ofthe fenceis the number of boards used to 
make it, and the height of the fenceis the length of each board in the fence. In the 
example fence below, the length of the fence is 4; the height of the fence is 50; 
and, the length of each piece of wood is shown:

Tudor would like to make the longest fence possible.  Please help him determine the 
maximumlength of any fence he could make, and the number of different heights a 
fence of that maximumlength could have.

Input Specification
The first line will contain the integer N (2 ≤ N ≤ 1000000).
The second line will contain N space-separated integers L1, L2, . . . , LN (1 ≤ Li ≤ 2000).
For 7 of the 15 available marks, N ≤ 100. For an additional 6 of the 15 available marks,
N ≤ 1000. For an additional 1 of the 15 available marks, N ≤ 100000.

Output Specification
Output two integers on a single line separated by a single space:  the length of the longest
fence and the number of different heights a longest fence could have. 

Sample Input 1
1 2 3 4
Output for Sample Input 1
2 1

Explanation for Output for Sample Input 1
Tudor first combines the pieces of wood with lengths 1 and 4 to form a board of length 5. 
Then he combines the pieces of wood with lengths 2 and 3 to form another board of length 5.  
Finally, he combines the boards to make a fence with length 2 and height 5.

Sample Input 2
1 10 100 1000 2000
Output for Sample Input 2
1 10

Explanation for Output for Sample Input 2
Tudor can’t make a fence longer than length 1, and there are 10 ways to make a fence with 
length 1 by choosing any two pieces of wood to nail together. Specifically, he may have
a fence of height 11, 101, 1001, 2001, 110, 1010, 2010, 1100, 2100, 3000
"""

import math 

raw_data = input()  # Sample Input 1: 1 2 3 4

# Generate a list of integers from the string
wood_lengths = [int(i) for i in raw_data.split()]
print("Converted to list of integers: ", wood_lengths)


# STEP 1 - Figure out the pattern:

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0) + all_woods.pop(0)]
# woods2 = [all_woods.pop(0) + all_woods.pop(0)]
# woods3 = [all_woods.pop(0) + all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0) + all_woods.pop(0)]
# woods2 = [all_woods.pop(0) + all_woods.pop(1)]
# woods3 = [all_woods.pop(0) + all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0) + all_woods.pop(0)]
# woods2 = [all_woods.pop(0) + all_woods.pop(2)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(1)]
# woods2 = [all_woods.pop(0), all_woods.pop(0)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(1)]
# woods2 = [all_woods.pop(0), all_woods.pop(1)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(1)]
# woods2 = [all_woods.pop(0), all_woods.pop(2)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)


# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(2)]
# woods2 = [all_woods.pop(0), all_woods.pop(0)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(2)]
# woods2 = [all_woods.pop(0), all_woods.pop(1)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(2)]
# woods2 = [all_woods.pop(0), all_woods.pop(2)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(3)]
# woods2 = [all_woods.pop(0), all_woods.pop(0)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(3)]
# woods2 = [all_woods.pop(0), all_woods.pop(1)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

# all_woods = wood_lengths.copy()
# woods1 = [all_woods.pop(0), all_woods.pop(3)]
# woods2 = [all_woods.pop(0), all_woods.pop(2)]
# woods3 = [all_woods.pop(0), all_woods.pop(0)]
# boards = ((woods1, woods2, woods3))
# fences.append(boards)

    
# print(fences)


# STEP 2 - Try it in nested loops (we know it will need recursion eventually)
# Alternate answer: Brute force!
def board_combinations(wood_lengths):
    """ 
    Given a list of wood lengths (e.g. [1,2,3,4]), find all possible board combinations
    Remember: wood = 1 piece, board = 2 pieces of wood.
    1 + 2 = 3 and 3 + 4 = 7
    1 + 3 and 2 + 4
    1 + 4 and 2 + 3
    Return a list of tuples for example: [(3, 7), (4, 6), (5, 5)]
    """

    n = len(wood_lengths)
    r = 2
    # number of possible combos of = n! / (r! (n - r)!)
    # 4! / (2!(4-2)!) = 24 / (2(2)!) = 24 / 4 = 6
    # num_combos = math.factorial(n) / (math.factorial(r)*math.factorial(n - r))
    # print(num_combos)

    fences = []
    for i in range(n-1):
        for j in range(n-3):
            for k in range(n-5):
                all_woods = wood_lengths.copy()
                boards = []
                boards.append(all_woods.pop(0) + all_woods.pop(i))
                boards.append(all_woods.pop(0) + all_woods.pop(j))
                boards.append(all_woods.pop(0) + all_woods.pop(k))
                # boards.append(all_woods.pop(0) + all_woods.pop(0))
                fences.append(tuple(boards))
        
    print("Fences: ", fences) 

# board_combinations(wood_lengths)


# https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways


# STEP 3 - RECURSION
fences = []  # global
next_fence = False  # global


def generate_fence(wood_lengths_remaining, original=True):
    global next_fence
    global fences

    n = len(wood_lengths_remaining)
    fence = []
    if n < 2:
        next_fence = True
        return []
    else:
        for i in range(n-1):
            fence += [wood_lengths_remaining.pop(0) + wood_lengths_remaining.pop(i)]
            fence += generate_fence(wood_lengths_remaining, False)

            if next_fence:
                wood_lengths_remaining = wood_lengths.copy()  # reset to try another fence.
                next_fence = False
                fences.append(fence)
                fence = []

    return fence


generate_fence(wood_lengths.copy())
print(list(fences))
# print(fences)

# print(combos)
# print(fences)

# def all_pairs(lst):
#     if len(lst) < 2:
#         yield []
#         return
#     if len(lst) % 2 == 1:
#         # Handle odd length list
#         for i in range(len(lst)):
#             for result in all_pairs(lst[:i] + lst[i+1:]):
#                 yield result
#     else:
#         a = lst.pop(0)
#         for i in range(len(lst)):
#             board = a + lst.pop(i)
#             for rest in all_pairs(lst.copy()):
#                 yield [board] + rest


# print(list(all_pairs(wood_lengths)))
