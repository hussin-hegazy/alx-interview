#!/usr/bin/python3

"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """
    Function to return the perimeter of the island described in grid.
    
    Parameters:
    grid (list of list of integers): The grid representing the island and water. 
    1 represents land, 0 represents water.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if the cell is land (1)
            if grid[row][col] == 1:
                # Add 4 for each land cell to the perimeter
                perimeter += 4

                # Check if the cell has a land neighbor to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

                # Check if the cell has a land neighbor above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

    return perimeter
