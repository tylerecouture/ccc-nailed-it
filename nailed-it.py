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

raw_data = input("Enter a space seperated list of wood pieces: (e.g: \"1 10 100 1000 2000\")")  # Sample Input 1: 1 2 3 4 5 6

# Generate a list of integers from the string
wood_lengths = [int(i) for i in raw_data.split()]
print("Converted to list of integers: ", wood_lengths)


def generate_fences(wood_list):
    """
    Find all possible board combos using (recursive generator function)

    Sample Input: wood_list = [1, 10, 100, 1000, 2000] 
    would return a generator equivalent to 
    [[110, 3000], [1010, 2100], [2010, 1100], [101, 3000], [1001, 2100], [2001, 1100], [11, 3000], 
    [1001, 2010], [2001, 1010], [11, 2100], [101, 2010], [2001, 110], [11, 1100], [101, 1010], [1001, 110]]
    
    """
    num_pieces_of_wood_left = len(wood_list)

    if num_pieces_of_wood_left == 2:  # if there are less than 2 pieces of wood left, then we're done this round
        # add them up to get board length and return as a single element list
        yield [wood_list[0] + wood_list[1]]

    elif num_pieces_of_wood_left % 2 == 0:  # even number of pieces that isn't exactly 2
        # We have at least 2 pieces of wood we need to pair up (and an even total number)

        # pop the first piece of wood off the list, and start pairing it up with other pieces of wood
        first = wood_list.pop(0)  # first: 1, wood_list: [10, 100, 1000, 2000] 

        # give each piece of wood an index with enumerate() https://docs.python.org/3/library/functions.html#enumerate
        # do this so we can put them back after each iterations
        # enumerate(wood_list): [(0, 10), (1, 100), (2, 1000), (3, 2000)]
        for i, wood_piece in enumerate(wood_list):  # i: 0, piece_of_wood: 10

            # pop off the second piece of wood, which will change for each iteration
            second = wood_list.pop(i)  # second: 10, wood_list: [100, 1000, 2000] 

            # Using recursion, get the list of boards (pairs) that can come from what's left
            # [100, 1000, 2000] --> [[1100], [2100], [3000]]]
            # With a longer list of wood pieces, this could be several nested lists deep

            # And loop through that list
            for list_of_boards in generate_fences(wood_list):  # first time through will be [1100]
                # insert the first board we already got, put it at the front
                list_of_boards.insert(0, (first + second))
                yield list_of_boards  # [11, 1100] for 1st iteration, [11, 2100] for 2nd, etc.
            wood_list.insert(i, second)  # put the second board back in it's original position
            # Continue iterations keeping first board constant

        # put the first board back in at the front.  We need it there because we poppoed it out
        # Doesn't do anything on the first time through, but when recursing, we need the list built back up again
        wood_list.insert(0, first)
    
    else:  # odd number of pieces of wood (this will only ever happen on the first pass)

        # remove one wood piece and get all the boards, then repeat, removing a different piece of wood each iteration
        # when each piece is removed, we're left with an even number of wood pieces, and all the combos are 
        # generated above
        for i, wood_piece in enumerate(wood_list):
            removed_piece = wood_list.pop(i) 
            for list_of_boards in generate_fences(wood_list):
                yield list_of_boards
            # put the wood back in its original position so we can pop a different one on the next iterations
            wood_list.insert(i, removed_piece)  


fences = generate_fences(wood_lengths)
print(list(fences))
