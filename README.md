# Purpose of the project
Project contains sudoku game that uses backtracking algorithm to: create new grids, check its validity and solve the board.

# Backtracking algorithm
Backtracking is a brut force algorithm that systematically searches for a solution to a problem among all available options. It does so by assuming that the solutions are represented by vectors (v1, ..., vm) of values and by traversing, in a depth first manner, the domains of the vectors until the solutions are found.

(source: Gurari, Eitan (1999). "CIS 680: DATA STRUCTURES: Chapter 19: Backtracking Algorithms". Archived from the original on 17 March 2007,
link:https://web.archive.org/web/20070317015632/http://www.cse.ohio-state.edu/~gurari/course/cis680/cis680Ch19.html#QQ1-51-128)

# Files description
- .gitignore - ignores certain files not to be included to repository.
- Graphics/ - folder with graphics for the project.
- main.py - runs the script and is responsible for the graphics of the game.
- positioning.py - calculates the positions of the elements on the GUI.
- random_function.py - produces random numbers in a interval.
- requirements.txt - displays necessary packages in order to run the script.
- sudoku.png - picture of the game.
- sudoku.py - contains main logic of the game.

# To improve
1. Better architecture of the project. Separate classes for positioning and improvement of Sudoku class (especially static and class methods).
2. Code optimization and standardization.
3. Generation of sudoku grits -> potentially connection to API that provides completely new grid every time.
4. Inconsistencies with private methods.
5. Hard-coded attributes.
