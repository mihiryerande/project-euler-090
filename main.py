# Problem 90:
#     Cube Digit Pairs
#
# Description:
#     Each of the six faces on a cube has a different digit (0 to 9) written on it;
#       the same is done to a second cube.
#     By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
#
#     For example, the square number 64 could be formed:
#         +---+  +---+
#         | 6 |  | 4 |
#         +---+  +---+
#
#     In fact, by carefully choosing the digits on both cubes
#       it is possible to display all of the square numbers below one-hundred:
#         01, 04, 09, 16, 25, 36, 49, 64, and 81.
#
#     For example, one way this can be achieved is by placing
#       {0, 5, 6, 7, 8, 9} on one cube and
#       {1, 2, 3, 4, 8, 9} on the other cube.
#
#    However, for this problem we shall allow the 6 or 9 to be turned upside-down
#      so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7}
#      allows for all nine square numbers to be displayed;
#      otherwise it would be impossible to obtain 09.
#
#     In determining a distinct arrangement we are interested in the digits on each cube, not the order.
#         {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#         {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
#
#     But because we are allowing 6 and 9 to be reversed,
#       the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
#       for the purpose of forming 2-digit numbers.
#
#     How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

from itertools import combinations


def main():
    """
    Returns the number of distinct arrangements of digits 0-9 on cubes
      which allows the formation of all squares less than 100,
      where 6 and 9 are considered interchangeable.

    Returns:
        (int): Number of arrangements of digits on cubes s.t. all squares < 100 can be formed.
    """

    # Idea:
    #     There are 10 possible digits (0 to 9, inclusive).
    #     A single cube has 6 faces, each with a different digit on it,
    #       producing (10 choose 6) = 210 possible distinct arrangements of digits on one cube.
    #     As there are 2 cubes, there are 210^2 = 44,100 arrangements of digits on two cubes.
    #     Also, since the order of cubes doesn't matter,
    #       we can roughly divide by 2 to get 7,056 / 2 = 3,528 ways.
    #
    #     Since this is a relatively small amount of arrangements to consider,
    #       we can simply iterate through them and count the number
    #       which allow for all the squares below 100 to be formed.
    #
    #     Also, hardcode some alterations to simply treat all 9's as 6's.

    # All square numbers as strings to be formed with cube faces
    # Treat any 9's as 6's for sake of number formation
    square_strs = ['{:02d}'.format(x ** 2).replace('9', '6') for x in range(1, 10)]

    # All digits, with 6 and 9 still considered different, apparently
    digits = [str(d) for d in range(10)]

    count = 0
    for cube_1 in combinations(digits, 6):
        faces_1 = set(cube_1)
        if '6' in faces_1:  # If 6 or 9 present, then both considered present
            faces_1.add('9')
        elif '9' in faces_1:
            faces_1.add('6')
        else:
            pass

        for cube_2 in combinations(digits, 6):
            if cube_1 <= cube_2:
                faces_2 = set(cube_2)
                if '6' in faces_2:  # If 6 or 9 present, then both considered present
                    faces_2.add('9')
                elif '9' in faces_2:
                    faces_2.add('6')
                else:
                    pass

                # Check if all squares can be formed with this cube arrangement
                count += all(map(lambda s: (s[0] in faces_1 and s[1] in faces_2) or
                                           (s[0] in faces_2 and s[1] in faces_1), square_strs))
            else:
                pass

    return count


if __name__ == '__main__':
    distinct_cube_arrangements = main()
    print('Number of distinct valid arrangements of digits on cubes to form square numbers:')
    print('  {}'.format(distinct_cube_arrangements))
