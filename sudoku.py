"""Responsible for main logic of Sudoku by generating sudoku board, checking the win conditions and auto filling the Board using backtracking algorithm"""

import copy
import random
from typing import Type, TypeVar
from random_function import random_inti

S = TypeVar('S', bound='Sudoku')

class Sudoku:
    """
    Description:
        Creates empty grid and performs Sudoku operations on it like: assigning number, deleting number, checking the validity of a grid, auto complete etc.
    """

    _object_registry = []
    _coordinates_registry = []
    board = [[0 for _ in range(1, 10)] for _ in range(1, 10)]
    objects_count = 0

    def __init__(self, x: int, y: int, number: int, grid: bool=False) -> None:
        """
        Description:
            Constructor for Sudoku class.

        Parameters:
            x - x coordinate.
            y - y coordinate.
            number - sudoku number placed on a grid.
            gird - indicates whether number is placed on a board by a player or by game (True - game, False - player).
        """

        switch = True  # this switch allows to assign a number to en empty square or when number is not given from
        # the beginning
        if (x, y) in Sudoku._coordinates_registry:
            for num, (object_x, object_y, _, object_grid) in enumerate(
                Sudoku.list_attributes()
            ):
                if x == object_x and y == object_y:
                    if object_grid == False:
                        del Sudoku._object_registry[num]
                    else:
                        switch = False

        if switch:
            self.x = x
            self.y = y
            self.number = number
            self.grid = grid
            self._object_registry.append(self)
            self._coordinates_registry.append((self.x, self.y))
            Sudoku.board[x - 1][y - 1] = number
            Sudoku.objects_count += 1

    @staticmethod
    def list_attributes() -> list[int, int, int, bool]:
        """
        Description:
            Provides lists of attributes of sudoku numbers placed on a board.
        
        Returns:
            The list of attributes of sudoku numbers.
        """

        objects_features = []
        for object in Sudoku._object_registry:
            objects_features.append((object.x, object.y, object.number, object.grid))

        return objects_features

    @classmethod
    def print_board(cls: Type[S]) -> None:
        """
        Description:
            Prints the board.
        """

        print("----------------------------------")
        for board in list(map(list, zip(*Sudoku.board))):
            print(board)

    @staticmethod
    def delete_item(x: int, y: int) -> None:
        """
        Description:
            Deletes a particular number from the board placed by a player of a coordinates (x,y).

        Parameters:
            x - x coordinate.
            y - y coordinate.
        """

        if (x, y) in Sudoku._coordinates_registry:
            for num, (object_x, object_y, _, object_grid) in enumerate(
                Sudoku.list_attributes()
            ):
                if x == object_x and y == object_y:
                    if object_grid == False:
                        del Sudoku._object_registry[num]
                        Sudoku.board[x - 1][y - 1] = 0
                        Sudoku.objects_count -= 1

    @staticmethod
    def delete_all() -> None:
        """
        Description:
            Deletes all numbers from the board placed by a player.
        """

        for object in [obj for obj in Sudoku._object_registry if obj.grid == False]:
            Sudoku.delete_item(object.x, object.y)

    @classmethod
    def remove_all_numbers(cls: Type[S]) -> None:
        """
        Description:
            Removes all numbers from a board.  
        """
        Sudoku._object_registry = []
        Sudoku.board = [[0 for _ in range(1, 10)] for _ in range(1, 10)]

    @classmethod
    def update_board(cls: Type[S],
        x: int=random_inti() - 1,
        y: int=random_inti() - 1,
        num: int=random_inti(),
    ) -> list[list[int]]:
        """
        Description:
            Places a random number number on a random Sudoku board.

        Parameters:
            x - x coordinate.
            y - y coordinate.
            num - number on Sudoku board.

        Returns:
           Updated Sudoku board by a random number from 0 to 9 on a random place on the board.
        """

        Sudoku.board[x][y] = num
        return Sudoku.board

    @classmethod
    def find_empty(cls: Type[S]) -> tuple[int, int]:
        """
        Description:
            Finds an empty square on the board.

        Returns:
            row - number that indicates position of a row.
            col - number that indicates position of a column.
        """
        for row, array in enumerate(Sudoku.board):
            for col, item in enumerate(array):
                if item == 0:
                    return row, col
    
    @classmethod
    def copy_board(cls: Type[S], grid_state: bool) -> None:
        """
        Description:
            Makes a copy of a board

        Parameters:
            grid_state - indicates whether number is placed on a board by a player or by game (True - game, False - player).
        """
        for row, array in enumerate(Sudoku.board):
            for col, item in enumerate(array):
                if item == 0:
                    pass
                else:
                    Sudoku(row + 1, col + 1, item, grid_state)

    @classmethod
    def solve_board(cls: Type[S]) -> bool:
        """
        Description:
            Solves the Sudoku Board.

        Parameters:
            board - sudoku board with numbers placed on it.

        Returns:
            (row, col) - position of row and column on a board.
        """
        position = Sudoku.find_empty()
        copy_board = copy.deepcopy(Sudoku.board)
        if not position:
            return True
        else:
            row, col = position

        for number in range(1, 10):
            copy_board[row][col] = number
            if check(copy_board):
                Sudoku(row + 1, col + 1, number)
                if Sudoku.solve_board():
                    return True

                Sudoku.board[row][col] = 0

        return False

    @classmethod
    def create_board(cls: Type[S]):
        """
        Description:
            Creates a sudoku board with randomly generated initial numbers.
        """
        def update_one():
            """
            Description:
                Updates a sudoku board with a randomly placed random number on it. 
            """
            x = random_inti() - 1
            y = random_inti() - 1
            while (x, y) in Sudoku._coordinates_registry:
                x = random_inti() - 1
                y = random_inti() - 1

            Sudoku(x, y, random_inti(), True)

        def remove_numbers(board: Sudoku.board, remove_amount: int) -> Sudoku.board:
            """
            Description:
                Removes a certain numbers of numbers from sudoku board.
                
            Parameters:
                board - sudoku board with numbers placed on it.
                remove_amount - number of sudoku numbers that will be removed from a board

            Return:
                Returns a board with certain amount of numbers removed.
            """
            row, col, r = len(board), len(board[0]), []
            spaces = [[x, y] for x in range(row) for y in range(col)]
            for _ in range(remove_amount):
                r = random.choice(spaces)
                board[r[0]][r[1]] = 0
                spaces.remove(r)

                # removing the object_attribute
                if Sudoku._object_registry:
                    for obj in Sudoku._object_registry:
                        if obj.x == r[0] and obj.y == r[1]:
                            Sudoku._object_registry.pop(Sudoku._object_registry.index(obj))

            return board

        remove_numbers(Sudoku.board, 81)
        update_one()

        while not Sudoku.solve_board():
            remove_numbers(Sudoku.board, 81)
            update_one()

        final_grid = remove_numbers(Sudoku.board, 61)
        Sudoku.board = final_grid

        return final_grid

def check(board: Sudoku.board) -> bool:
    """
    Description:
        Verifies if the board has duplicates horizontally, vertically and per squares.

    Parameters:
        board - sudoku board with numbers placed on it.

    Returns:
        Boolean that indicates if duplicates are present.
    """

    def check_horizontally(board: Sudoku.board) -> bool:
        """
        Description:
            Verifies if the board has duplicates horizontally.

        Parameters:
            board - sudoku board with numbers placed on it.

        Returns:
            Boolean that indicates if duplicates are present in rows.
        """

        horizontal_bool = True
        for array in board:
            number_dict = {}
            for item in array:
                if item == 0:
                    pass
                else:
                    if item in number_dict.keys():
                        horizontal_bool = False
                        return horizontal_bool 
                    else:
                        number_dict[item] = 1
        return horizontal_bool

    def check_vertically(board: Sudoku.board) -> bool:
        """
        Description:
            Verifies if the board has duplicates vertically.

        Parameters:
            board - sudoku board with numbers placed on it.

        Returns:
            Boolean that indicates if duplicates are present in columns.
        """

        board_inverted = []
        columns_number = len(board)
        for number in range(columns_number):
            array_inverted = []
            for array in board:
                array_inverted.append(array[number])
            board_inverted.append(array_inverted)

        vertical_bool = check_horizontally(board_inverted)
        return vertical_bool

    def check_squares(board: Sudoku.board) -> bool:
        """
        Description:
            Verifies if the board has duplicates per squares. 

        Parameters:
            board - sudoku board with numbers placed on it.

        Returns:
            Boolean that indicates if duplicates are present in squares.

        Acknowledgements:
            GPT-3 helped to optimize this function.
        """

        squares = []
        for i in range(3):
            for j in range(3):
                square = [
                    board[r][c]
                    for r in range(i * 3, i * 3 + 3)
                    for c in range(j * 3, j * 3 + 3)
                ]
                squares.append(square)

        # Check the squares horizontally
        square_bool = check_horizontally(squares)
        return square_bool

    horizontal_bool = check_horizontally(board)
    vertical_bool = check_vertically(board)
    square_bool = check_squares(board)

    return horizontal_bool and vertical_bool and square_bool
