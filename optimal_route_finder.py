"""
Portfolio Project for CS 325, Summer 2023

This Python code employs a recursive depth-first search approach to find the minimum path 
through a grid-based board with obstacles, from a specified source point to a destination point.
"""


def solve_puzzle(board: list[list[str]], source: tuple[int], destination: tuple[int]) -> list[tuple[int], str]:
    """
    A function that takes as parameters a matrix representing a board with passable and impassable cells,
    a tuple representing the starting point on the board, and a tuple representing the ending point on the board.
    This function returns a list containing a list of tuples representing the minimum path and a string
    representing the movements on the board.  If no path from source to destination is possible, None is returned.
    """

    rows, columns = len(board), len(board[0])

    # source and Destianation are equal
    if source == destination:
        return [source]

    def solve_puzzle_helper(current: tuple[int], destination: tuple[int], path: list) -> tuple[int, tuple]:
        # Base case: destination reached
        if current == destination:
            return 0, [current]

        # Base case: current cell is not passable
        # Prevents min_distance and path from being updated
        curr_row, curr_col = current
        if board[curr_row][curr_col] == '#':
            return None, []

        min_distance = float('inf')
        min_path = []
        adjacent_cells = []

        # populate adjacent_cells with valid adjacent cells
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < rows and 0 <= new_y < columns:
                adjacent_cells.append((new_x, new_y))

        for cell in adjacent_cells:
            if cell not in path:
                distance, curr_path = solve_puzzle_helper(cell, destination, path + [current])

                # update min distance and path as necessary
                if distance is not None and distance + 1 < min_distance:
                    min_distance = distance + 1
                    min_path = curr_path

        return min_distance, [current] + min_path if min_path else None

    _, minimum_path = solve_puzzle_helper(source, destination, [])

    # No viable path
    if minimum_path is None:
        return None

    # Generate direction string (Extra Credit)
    direction_string = []
    for i in range(1, len(minimum_path)):
        last_cell, curr_cell = minimum_path[i - 1], minimum_path[i]

        # evaluate for up/down movement
        if last_cell[0] != curr_cell[0]:
            direction_string.append('U' if last_cell[0] > curr_cell[0] else 'D')

        # evaluate for left/right movement
        if last_cell[1] != curr_cell[1]:
            direction_string.append('L' if last_cell[1] > curr_cell[1] else 'R')

    return [minimum_path, "".join(direction_string)]
