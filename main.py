"""Responsible for graphics of the game and runs the script."""

import pygame
import os
from positioning import position
from sudoku import *
import sys
import sudoku

sys.setrecursionlimit(1000000)
SIZE = WIDTH, HEIGHT = 900, 435
SCREEN = pygame.display.set_mode(SIZE)
COLOR = (159, 44, 44)
FPS = 160

pygame.font.init()
FONT = pygame.font.SysFont("verdana", 22, True)
FONT_TITLE = pygame.font.SysFont("verdana", 33, True)
MENU_TEXT = FONT_TITLE.render("GAME MENU", True, (0, 0, 0))
CONGRATULATIONS_TEXT = FONT_TITLE.render("Congratulations, you win!", True, (0, 0, 0))
Y_TEXT = FONT_TITLE.render("Play Again!", True, (0, 0, 0))
N_TEXT = FONT_TITLE.render("Quit", True, (0, 0, 0))
ARROWS_TEXT = FONT.render("Move Cursor", True, (0, 0, 0))
NUMBER_TEXT = FONT.render("Type Number", True, (0, 0, 0))
BACKSPACE_TEXT = FONT.render("Delete One", True, (0, 0, 0))
DELETE_TEXT = FONT.render("Delete All", True, (0, 0, 0))
ENTER_TEXT = FONT.render("Verify", True, (0, 0, 0))
TAB_TEXT = FONT.render("Autocomplete", True, (0, 0, 0))

pygame.display.set_caption("Sudoku Solver")  # changes the name of the window

# graphics
GRID = pygame.image.load(
    os.path.join("Graphics", "General", "sudoku_grid.png")
)  # loads a grid
SUDOKU_ICON = pygame.image.load(
    os.path.join("Graphics", "General", "sudoku_icon.png")
)  # loads a icon
CURSOR = pygame.image.load(os.path.join("Graphics", "General", "cursor.xcf"))
pygame.display.set_icon(SUDOKU_ICON)  # uses the picture as a icon


ARROWS = pygame.image.load(os.path.join("Graphics", "Menu", "arrows.png"))
NUMBER = pygame.image.load(os.path.join("Graphics", "Menu", "number.png"))
BACKSPACE = pygame.image.load(os.path.join("Graphics", "Menu", "backspace.png"))
DELETE = pygame.image.load(os.path.join("Graphics", "Menu", "delete.png"))
ENTER = pygame.image.load(os.path.join("Graphics", "Menu", "enter.png"))
TAB = pygame.image.load(os.path.join("Graphics", "Menu", "tab.png"))

CONGRATULATIONS = pygame.image.load(
    os.path.join("Graphics", "Win", "congratulations.xcf")
)
Y_KEY = pygame.image.load(os.path.join("Graphics", "Win", "y.png"))
N_KEY = pygame.image.load(os.path.join("Graphics", "Win", "n.png"))

number_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def draw_window(x: int, y: int, end: bool) -> None:
    """
    Description:
        Controls the graphic element of the game.
    """

    SCREEN.fill(COLOR)  # this only works if you update the display
    SCREEN.blit(
        GRID, (0, 0)
    )  # this draws object on the screen; in pygame 0,0 coordinates is top left corner
    SCREEN.blit(CURSOR, position(x, y, True))  # shows selector on a stream

    # Printing menu text
    SCREEN.blit(MENU_TEXT, (565, 27))

    # Printing menu icons
    SCREEN.blit(ARROWS, (550, 110))
    SCREEN.blit(NUMBER, (550, 160))
    SCREEN.blit(BACKSPACE, (550, 210))
    SCREEN.blit(DELETE, (550, 260))
    SCREEN.blit(ENTER, (550, 310))
    SCREEN.blit(TAB, (550, 360))

    # Printing descriptions of the keys
    SCREEN.blit(ARROWS_TEXT, (600, 110))
    SCREEN.blit(NUMBER_TEXT, (600, 160))
    SCREEN.blit(BACKSPACE_TEXT, (600, 210))
    SCREEN.blit(DELETE_TEXT, (600, 260))
    SCREEN.blit(ENTER_TEXT, (600, 310))
    SCREEN.blit(TAB_TEXT, (600, 360))

    final = []
    final.extend(
        [
            (object.x, object.y, object.number, object.grid)
            for object in Sudoku._object_registry
            if object.grid == True
        ]
    )

    for l in range(9):
        for ll in range(9):
            if (l + 1, ll + 1, Sudoku.board[l][ll], True) not in final:
                final.append((l + 1, ll + 1, Sudoku.board[l][ll], False))
    for x, y, num, grid in final:
        if grid:
            if num == 0:
                pass
            else:
                func = pygame.image.load(
                    os.path.join("Graphics", "Grid_Numbers", number_dict[num] + ".png")
                )
                SCREEN.blit(func, position(x, y, False))
        else:
            if num == 0:
                pass
            else:
                func = pygame.image.load(
                    os.path.join("Graphics", "Numbers", number_dict[num] + ".png")
                )
                SCREEN.blit(func, position(x, y, False))

    if end:
        SCREEN.blit(CONGRATULATIONS, (150, 72))
        SCREEN.blit(CONGRATULATIONS_TEXT, (217, 104))
        SCREEN.blit(Y_KEY, (217, 229))
        SCREEN.blit(Y_TEXT, (259, 224))
        SCREEN.blit(N_KEY, (517, 229))
        SCREEN.blit(N_TEXT, (559, 224))
        pygame.display.update()
    pygame.display.update()  # updated to change the color of the background


def _prints_board() -> None:
    """
    Description:
        Prints a Sudoku board with initial numbers.
    """

    d = Sudoku.create_board()
    Sudoku.delete_all()
    Sudoku.copy_board(grid_state=True)


def main() -> None:
    """
    Description:
        Creates a main loop of the game.
    """

    clock = pygame.time.Clock()  # allows to slow down the while loop / FPS
    game = True  # sets the main loop of the game
    x, y = 1, 1  # initial coordinates of the selector
    _prints_board()
    end = False

    while game:

        clock.tick(FPS)  # controls the speed of a while loop
        # lets loop through the events and based on the events we can perform action

        for event in pygame.event.get():
            # this allows us to exit the game by clicking the cross

            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if x + 1 > 9:
                        x = 1
                    else:
                        x, y = x + 1, y

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if x - 1 < 1:
                        x = 9
                    else:
                        x, y = x - 1, y

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if y - 1 < 1:
                        y = 9
                    else:
                        x, y = x, y - 1

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if y + 1 > 9:
                        y = 1
                    else:
                        x, y = x, y + 1

                if event.key == pygame.K_1:
                    Sudoku(x, y, 1)
                if event.key == pygame.K_2:
                    Sudoku(x, y, 2)
                if event.key == pygame.K_3:
                    Sudoku(x, y, 3)
                if event.key == pygame.K_4:
                    Sudoku(x, y, 4)
                if event.key == pygame.K_5:
                    Sudoku(x, y, 5)
                if event.key == pygame.K_6:
                    Sudoku(x, y, 6)
                if event.key == pygame.K_7:
                    Sudoku(x, y, 7)
                if event.key == pygame.K_8:
                    Sudoku(x, y, 8)
                if event.key == pygame.K_9:
                    Sudoku(x, y, 9)

                if event.key == pygame.K_BACKSPACE:
                    Sudoku.delete_item(x, y)
                if event.key == pygame.K_DELETE:
                    Sudoku.delete_all()
                if event.key == pygame.K_ESCAPE:
                    game = False

                if event.key == pygame.K_RETURN:
                    check_if_good = sudoku.check(Sudoku.board)
                    if check_if_good:
                        numbers_board = []
                        for array in Sudoku.board:
                            numbers_board.extend(array)
                        if 0 not in numbers_board:
                            print("Congratulations! You win!")
                            end = True

                        else:
                            print("You are on the right track, keep working!")
                    else:
                        print("You have duplicates! Recheck your sudoku.")
                if event.key == pygame.K_TAB:
                    Sudoku.delete_all()
                    Sudoku.solve_board()

                if end == True:
                    if event.key == pygame.K_y:
                        end = False
                        Sudoku.remove_all_numbers()
                        _prints_board()

                    if event.key == pygame.K_n:
                        game = False

        draw_window(x, y, end)

    pygame.quit()


if __name__ == "__main__":
    # runs the script of this file and not of imported files
    main()
