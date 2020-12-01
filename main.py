import sodoku_solver

if __name__ == '__main__':
    problem = [
        [4,0,0, 8,7,0, 0,2,0],
        [0,8,0, 0,0,0, 4,0,0],
        [0,0,6, 3,0,0, 8,0,1],
        [7,0,0, 1,0,0, 0,8,0],
        [6,1,2, 0,9,8, 7,3,4],
        [0,0,0, 0,6,0, 0,1,9],
        [1,9,3, 4,2,7, 5,0,0],
        [8,0,7, 0,1,0, 3,0,2],
        [0,2,0, 0,0,3, 0,0,0]
    ]
    problem_copy = [
        [4,0,0, 8,7,0, 0,2,0],
        [0,8,0, 0,0,0, 4,0,0],
        [0,0,6, 3,0,0, 8,0,1],
        [7,0,0, 1,0,0, 0,8,0],
        [6,1,2, 0,9,8, 7,3,4],
        [0,0,0, 0,6,0, 0,1,9],
        [1,9,3, 4,2,7, 5,0,0],
        [8,0,7, 0,1,0, 3,0,2],
        [0,2,0, 0,0,3, 0,0,0]
    ]

    solver = sodoku_solver.SudokuSolver()
    solver.solve_basic(problem)
    print(*problem, sep = "\n")
    print(solver.recursions_basic)

    solver.solve_mrv(problem_copy)
    print(*problem_copy, sep = "\n")
    print(solver.recursions_mrv)

