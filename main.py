import sodoku_solver

if __name__ == '__main__':
    problem_copy = [
        [0,8,9, 7,5,0, 0,0,0],
        [5,0,0, 0,3,0, 0,0,0],
        [3,0,7, 0,0,6, 0,0,0],
        [7,0,0, 0,0,5, 3,0,0],
        [8,2,0, 0,0,0, 0,9,5],
        [0,0,5, 2,0,0, 0,0,1],
        [0,0,0, 4,0,0, 7,0,6],
        [0,0,0, 0,9,0, 0,0,3],
        [0,0,0, 0,7,3, 8,1,0]
    ]
    problem = [
        [0,8,9, 7,5,0, 0,0,0],
        [5,0,0, 0,3,0, 0,0,0],
        [3,0,7, 0,0,6, 0,0,0],
        [7,0,0, 0,0,5, 3,0,0],
        [8,2,0, 0,0,0, 0,9,5],
        [0,0,5, 2,0,0, 0,0,1],
        [0,0,0, 4,0,0, 7,0,6],
        [0,0,0, 0,9,0, 0,0,3],
        [0,0,0, 0,7,3, 8,1,0]
    ]

    solver = sodoku_solver.SudokuSolver()
    solver.solve_basic(problem)
    print(*problem, sep = "\n")
    print(solver.recursions_basic)

    solver.solve_mrv(problem_copy)
    print(*problem_copy, sep = "\n")
    print(solver.recursions_mrv)

