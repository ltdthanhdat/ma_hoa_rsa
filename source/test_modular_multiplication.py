# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import unittest
from modular_calculation import modular_multiplication
class Testmodular_multiplication(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(modular_multiplication(2, 3, 5), 1)
        self.assertEqual(modular_multiplication(10, 10, 7), 2)
        
    def test_large_numbers(self):
        self.assertEqual(modular_multiplication(123456789123456789, 987654321987654321, 999999937), 827637387)
        self.assertEqual(modular_multiplication(999999999999999999, 888888888888888888, 777777777), 0)
        
    def test_zero(self):
        self.assertEqual(modular_multiplication(0, 12345, 6789), 0)
        self.assertEqual(modular_multiplication(12345, 0, 6789), 0)
        self.assertEqual(modular_multiplication(0, 0, 6789), 0)
        
    def test_mod_one(self):
        self.assertEqual(modular_multiplication(12345, 67890, 1), 0)
        self.assertEqual(modular_multiplication(0, 67890, 1), 0)
        self.assertEqual(modular_multiplication(12345, 0, 1), 0)

if __name__ == '__main__':
    unittest.main()
