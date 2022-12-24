"""Contains function that produces a random number from 1 to 9"""

import random

def random_inti() -> int:
    """
    Description:
        Produces random integer in range(1,9).

    Returns:
        rand - integer in range(1,9).
    """

    rand = random.randint(1, 9)
    return rand