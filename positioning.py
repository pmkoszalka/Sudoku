"""Responsible for positioning of grid and figures on graphical user interface."""

import math

BEGINNING_LINE = 8
THIN_LINE = 1
THICK_LINE = 4
HORIZONTAL_LINE_RECTANGLE = 47
VERTICAL_LINE_RECTANGLE = 45
NUMBER_SIZE = 22


def calculate_place(position: int, req_dist:int) -> int:
    """
    Description:
        Calculates the length of all squares to a sudoku number.

    Parameters:
        position - number of a square that sudoku number is placed in.

    Returns:
        Number of pixels that has to be included while crossing the thick line on GUI.
    """

    return (position - 1) * req_dist


def calculate_thin_lines(position: int) -> int:
    """
    Description:
        Calculates the length of all thin lines to a sudoku number.

    Parameters:
        position - number of a square that a sudoku number is placed in.

    Returns:
        Number of pixels that has to be included while crossing the thin line on GUI.
    """
    if position == 1:
        return 0
    elif (position - 1) % 3 == 0:
        return calculate_thick_lines(position - 1)
    else:
        if position < 4:
            return position - 1
        elif position < 7:
            return position - 2
        else:
            return position - 3


def calculate_thick_lines(position: int) -> int:
    """
    Description:
        Calculates the length of all thick lines to sudoku number.

    Parameters:
        position - number of a square that sudoku number is placed in.

    Returns:
        Number of pixels that has to be included while crossing the thick line on GUI.
    """

    if position == 4:
        return math.floor((position - 1) / 3) * THICK_LINE + 1
    else:
        return math.floor((position - 1) / 3) * THICK_LINE


def position(
    position_down: int,
    position_right: int,
    selector: bool,
) -> tuple[int, int]:
    """
    Description:
        Calculates the total length to sudoku number.

    Parameters:
        position_down - number of a square that sudoku number is placed in vertically; starting from the top and counting down.
        position_right - number of a square that sudoku number is placed in vertically; starting from the top and counting right.
        selector - if the position is established for selector (True) or number (False).

    Return:
        (x,y) of the number on the coordinate plane.
    """

    if selector:
        beginning_distance_down = BEGINNING_LINE
        beginning_distance_right = BEGINNING_LINE

    else:
        beginning_distance_down = BEGINNING_LINE + math.floor(
            (HORIZONTAL_LINE_RECTANGLE - NUMBER_SIZE) / 2
        )
        beginning_distance_right = BEGINNING_LINE + math.floor(
            (HORIZONTAL_LINE_RECTANGLE - NUMBER_SIZE) / 2
        )

    position_down = (
        beginning_distance_down
        + calculate_place(position_down, HORIZONTAL_LINE_RECTANGLE)
        + calculate_thin_lines(position_down)
        + calculate_thick_lines(position_down)
    )
    position_right = (
        beginning_distance_right
        + calculate_place(position_right, VERTICAL_LINE_RECTANGLE)
        + calculate_thin_lines(position_right)
        + calculate_thick_lines(position_right)
    )

    return position_down, position_right
