#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """ Solve the N Queens problem using backtracking """
    if col >= len(board):
        solutions.append([list(row) for row in board])
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0
    return False


def print_solutions(solutions):
    """ Print all solutions in the required format """
    for solution in solutions:
        formatted_solution = []
        for i in range(len(solution)):
            for j in range(len(solution)):
                if solution[i][j] == 1:
                    formatted_solution.append([i, j])
        print(formatted_solution)


def nqueens(N):
    """ Main function to solve the N Queens problem """
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)


if __name__ == "__main__":
    main()
