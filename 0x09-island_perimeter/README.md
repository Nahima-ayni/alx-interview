Island Perimeter Problem - Notes
Objective: Calculate the perimeter of a single island in a 2D grid, where:

0 = Water
1 = Land
Approach:

Grid Iteration: Use nested loops to iterate over each cell in the grid.
Perimeter Calculation:
For each land cell (grid[i][j] == 1), check its four neighbors (top, bottom, left, right).
Add to the perimeter if the neighbor is water (0) or the cell is on the boundary of the grid.
