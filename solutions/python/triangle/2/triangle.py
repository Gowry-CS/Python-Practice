def validity(sides):
    """
    Determine if the given side lengths can form a valid triangle.

    :param sides: list of three numbers - the side lengths of the triangle.
    :return: bool - True if the side lengths satisfy the triangle inequality, False otherwise.
    """

    
    return (
        sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and
        sides[0] + sides[1] >= sides[2] and
        sides[1] + sides[2] >= sides[0] and
        sides[0] + sides[2] >= sides[1]
    )

def equilateral(sides):
    """
    Determine if a triangle is equilateral.

    :param sides: list of three numbers - the side lengths of the triangle.
    :return: bool - True if all sides are equal, False otherwise.
    """

    return (
        validity(sides) and
        len(set(sides)) == 1
    )


def isosceles(sides):
    """
    Determine if a triangle is isosceles.

    :param sides: list of three numbers - the side lengths of the triangle.
    :return: bool - True if at least 2 sides are equal, False otherwise.
    """

    return (
        validity(sides) and
        len(set(sides)) <= 2
    )


def scalene(sides):
    """
    Determine if a triangle is scalene.

    :param sides: list of three numbers - the side lengths of the triangle.
    :return: bool - True if all sides are not equal, False otherwise.
    """

    return (
        validity(sides) and
        len(set(sides)) == 3
    )
