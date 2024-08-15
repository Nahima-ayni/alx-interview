0x07 - Rotate 2D Matrix
Overview
This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The task requires a solid understanding of matrix manipulation, in-place operations, and algorithmic efficiency in Python. The challenge tests your ability to handle 2D data structures and optimize space complexity.

Key Concepts
Matrix Representation in Python

In Python, a 2D matrix is typically represented as a list of lists, where each sublist represents a row.
Accessing matrix elements is done using double indices, e.g., matrix[i][j].
In-place Operations

In-place operations modify the data structure without creating a new one, optimizing space complexity.
This task requires performing the matrix rotation in-place, meaning no additional matrix should be created.
Matrix Transposition

Transposing a matrix involves swapping its rows and columns.
For a given element at position (i, j), after transposition, it will be at position (j, i).
Reversing Rows

After transposing, to achieve a 90-degree clockwise rotation, each row of the matrix needs to be reversed.
Nested Loops

Nested loops are used to iterate through the matrix elements.
Proper use of nested loops is essential for transposing and reversing the rows in the matrix.
Steps to Rotate the Matrix
Transpose the Matrix

Swap the element at position (i, j) with the element at position (j, i) for all i < j.
This converts rows into columns and columns into rows.
Reverse Each Row

After transposition, reverse each row to achieve the 90-degree clockwise rotation.
The reversal turns the first row into the last column, the second row into the second last column, and so on.
Example
Given the following 3x3 matrix:

Copy code
1 2 3
4 5 6
7 8 9
Step 1: Transpose the matrix

Copy code
1 4 7
2 5 8
3 6 9
Step 2: Reverse each row

Copy code
7 4 1
8 5 2
9 6 3
The matrix has been rotated 90 degrees clockwise.
