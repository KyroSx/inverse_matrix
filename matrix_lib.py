def is_valid_column_row(row: int, column: int) -> bool:
    if type(row) is int and type(column) is int:
        if row > 0 and column > 0:
            return True
    return False


def create_full_zeros_matrix(row: int, column: int) -> list:
    if is_valid_column_row(row, column):
        matrix = [[0] * column] * row

        return matrix


def create_random_matrix(row: int, column: int) -> list:
    import random

    if is_valid_column_row(column, row):
        matrix = []
        for _ in range(row):
            row = []
            for __ in range(column):
                value = random.randint(1, 10)
                row.append(value)
            matrix.append(row)
        return matrix


def sum_two_lists(first: list, second: list) -> list:
    size = len(first)
    result = []

    for index in range(size):
        value_summed = first[index] + second[index]
        result.append(value_summed)

    return result


def multiply_two_matrix(first: list,
                        second: list):
    zip_second = zip(*second)
    zip_second = list(zip_second)

    result = [
        [sum(
            element_first*element_second
            for element_first, element_second in zip(row_first, column_second)
        ) for column_second in zip_second
        ] for row_first in first
    ]

    return result


def print_matrix(matrix) -> None:
    column_len = len(matrix[0])
    row_len = len(matrix)

    for row in range(row_len):
        for column in range(column_len):
            value = matrix[row][column]
            print(f'[{value}]', end='')
        print()
