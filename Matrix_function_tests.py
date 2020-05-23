import unittest
from matrix_lib import *


class TestMatrix(unittest.TestCase):
    def test_random_matrix(self):
        ''' Should return a correct matrix with those dimensions '''
        row = 2
        col = 3
        matrix = create_random_matrix(row, col)

        column_len = len(matrix[0])
        row_len = len(matrix)

        self.assertEqual(row_len, 2)
        self.assertEqual(column_len, 3)

        ''' All elements in the matrix should be less or equal 10 '''
        for row in range(row_len):
            for column in range(column_len):
                value = matrix[row][column]
                self.assertLessEqual(value, 10)

    def test_sum_two_lists(self):
        ''' Should return the correct list '''
        x = [1, 1, 1]
        y = [2, 2, 2]

        response = sum_two_lists(x, y)
        result = [3, 3, 3]

        self.assertListEqual(response, result)

    def test_multiply_two_matrix(self):
        ''' should return correct multiplication matrix '''
        a = [[-8, 4, -6, 1],
             [2, -5, 7, 3]]
        b = [[0, 4],
             [2, -2],
             [1, -5],
             [3, 8]]

        response = multiply_two_matrix(a, b)

        result = [[5, -2],
                  [6, 7]]

        self.assertListEqual(response, result)

        ''' should return correct matrix dimensions '''
        row_a = len(a)
        col_b = len(b[0])

        self.assertEqual(len(response), row_a)
        self.assertEqual(len(response[0]), col_b)
