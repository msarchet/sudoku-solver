class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class PositionWithValues:
    def __init__(self, position=Position(0, 0), values=[]):
        self.position = position
        self.values = values


class SudokuSolver:
    def __init__(self):
        self.recursions_basic = 0
        self.recursions_mrv = 0

    def solve_basic(self, board, reset_recursions=False):
        if reset_recursions:
            self.recursions_basic = 0

        self.recursions_basic += 1

        zero_position = self.get_first_zero(board)
        if zero_position is None:
            return True

        possibles = self.get_possible_values(board, zero_position)

        for possible in possibles:
            board[zero_position.row][zero_position.column] = possible
            if self.solve_basic(board):
                return True
            board[zero_position.row][zero_position.column] = 0

        return False

    def solve_mrv(self, board, reset_recursions=False):
        if reset_recursions:
            self.recursions_mrv = 0

        self.recursions_mrv += 1
        lowest_score_pair: PositionWithValues = None
        for score_pair in self.get_zero_scores(board):
            if lowest_score_pair is None \
                    or len(score_pair.values) <= len(lowest_score_pair.values):
                lowest_score_pair = score_pair

        if lowest_score_pair is None:
            return True

        position = lowest_score_pair.position
        for possible in lowest_score_pair.values:
            board[position.row][position.column] = possible
            if self.solve_mrv(board):
                return True
            board[position.row][position.column] = 0

        return False

    def get_zero_scores(self, board):
        for row in range(9):
            for column in range(9):
                if board[row][column] == 0:
                    position = Position(row, column)
                    values = self.get_possible_values(board, position)
                    yield PositionWithValues(position, list(values))

    def get_first_zero(self, board):
        row = 0
        while row < 9:
            column = 0
            while column < 9:
                if board[row][column] == 0:
                    return Position(row, column)
                column += 1
            row += 1
        return None

    def get_possible_values(self, board, position):
        box_row_start = position.row // 3 * 3
        box_column_start = position.column // 3 * 3
        box_row_end = box_row_start + 3
        box_column_end = box_column_start + 3

        values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for row in range(9):
            for column in range(9):
                if row == position.row or column == position.column \
                        or (box_row_start <= row < box_row_end and box_column_start <= column < box_column_end):
                    if board[row][column] != 0:
                        values.discard(board[row][column])
        for value in values:
            yield value
