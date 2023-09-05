#!/usr/bin/env python3
'''
0x09 island perimeter
'''


def island_perimeter(grid):
    '''
    a function that retruns the perimeter of the island in the grid
    '''
    # Initialize the perimeter variable to keep track of the total perimeter
    perimeter = 0

    # four possible directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the cell is land
            if grid[row][col] == 1:
                # Initialize the count of neighboring land cells
                neighbors = 0

                # Check each direction
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check if neighboring cell is within bounds & is also land
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        neighbors += 1

                # Add the contribution of this cell to the perimeter
                # contribution is 4 minus the number of neighboring land cells
                perimeter += 4 - neighbors

    return perimeter
