# 0x05. N Queens

## Table of Contents
1. [Introduction](#introduction)
2. [Project Requirements](#project-requirements)
3. [Key Concepts](#key-concepts)
   - [Backtracking Algorithms](#backtracking-algorithms)
   - [Recursion](#recursion)
   - [List Manipulations in Python](#list-manipulations-in-python)
   - [Python Command Line Arguments](#python-command-line-arguments)
4. [Implementation Steps](#implementation-steps)
5. [Resources](#resources)
6. [Conclusion](#conclusion)

## Introduction
The N Queens problem is a classic puzzle where the goal is to place N queens on an N×N chessboard such that no two queens can attack each other. This project requires implementing a solution using the backtracking algorithm in Python. The task is to explore all potential solutions and backtrack when a partial solution cannot be extended to a full solution.

## Project Requirements
- Implement a function to solve the N Queens problem using backtracking.
- Use recursion to explore potential solutions.
- Manipulate lists to store the positions of the queens.
- Handle command-line arguments to specify the size of the board (N).

## Key Concepts

### Backtracking Algorithms
Backtracking is a general algorithmic technique that considers searching every possible combination to solve a computational problem. If a solution is not feasible, the algorithm backtracks and tries another possibility.

#### Resources:
- [Backtracking Introduction](https://www.geeksforgeeks.org/backtracking-introduction/)
- [Understanding Backtracking Algorithms](https://www.freecodecamp.org/news/backtracking-algorithm-explained/)

### Recursion
Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. In the N Queens problem, recursion is used to place queens one by one in different rows.

#### Resources:
- [Recursion in Python](https://www.programiz.com/python-programming/recursion)
- [Python Recursion Explained](https://realpython.com/python-thinking-recursively/)

### List Manipulations in Python
Lists are a fundamental data structure in Python. You'll need to create and manipulate lists to store the positions of the queens on the board.

#### Resources:
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [List Methods in Python](https://www.programiz.com/python-programming/methods/list)

### Python Command Line Arguments
Command-line arguments allow you to provide input values to your script from the terminal. In this project, you'll handle the board size input using command-line arguments.

#### Resources:
- [Command Line Arguments in Python](https://www.geeksforgeeks.org/python-command-line-arguments/)
- [Using sys.argv](https://www.pythonforbeginners.com/system/python-sys-argv)

## Implementation Steps
1. **Initialize the Board**: Create an N×N board represented as a list of lists.
2. **Place Queens**: Use a recursive function to place queens on the board.
3. **Check Safety**: Implement a function to check if a queen can be placed at a given position without being attacked.
4. **Backtracking**: If placing a queen leads to a conflict, backtrack and try the next position.
5. **Handle Command-Line Arguments**: Use `sys.argv` to take the board size N as input from the command line.
6. **Print Solutions**: Once a solution is found, print the board configuration.

## Resources
- **Backtracking Algorithms**:
  - [Backtracking Introduction](https://www.geeksforgeeks.org/backtracking-introduction/)
  - [Understanding Backtracking Algorithms](https://www.freecodecamp.org/news/backtracking-algorithm-explained/)
- **Recursion**:
  - [Recursion in Python](https://www.programiz.com/python-programming/recursion)
  - [Python Recursion Explained](https://realpython.com/python-thinking-recursively/)
- **List Manipulations in Python**:
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
  - [List Methods in Python](https://www.programiz.com/python-programming/methods/list)
- **Python Command Line Arguments**:
  - [Command Line Arguments in Python](https://www.geeksforgeeks.org/python-command-line-arguments/)
  - [Using sys.argv](https://www.pythonforbeginners.com/system/python-sys-argv)

## Conclusion
The N Queens problem is an excellent exercise to improve your algorithmic thinking and programming skills. By understanding and implementing backtracking, recursion, and list manipulations, you can develop an efficient solution. Make sure to utilize the provided resources to deepen your understanding of these concepts.

---
