# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import unittest
from modular_calculation import modular_exponentiation
class TestModularExponentiation(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(modular_exponentiation(2, 3, 5), 3)
        self.assertEqual(modular_exponentiation(3, 3, 7), 6)
        self.assertEqual(modular_exponentiation(4, 2, 9), 7)
        
    def test_large_numbers(self):
        self.assertEqual(modular_exponentiation(10123465234878998, 123456789, 10005412336548794), 8080341694206197)
        self.assertEqual(modular_exponentiation(987654321, 123456789, 1000000007), 652541198)
        self.assertEqual(modular_exponentiation(987654321987654321, 987654321, 999999937), 142857143)
        
    def test_zero_exponent(self):
        self.assertEqual(modular_exponentiation(5, 0, 3), 1) 
        self.assertEqual(modular_exponentiation(10, 0, 7), 1)
        
    def test_zero_base(self):
        self.assertEqual(modular_exponentiation(0, 5, 3), 0)
        self.assertEqual(modular_exponentiation(0, 10, 7), 0)
        
    def test_modulus_one(self):
        self.assertEqual(modular_exponentiation(12345, 67890, 1), 0)  
        self.assertEqual(modular_exponentiation(987654321, 123456789, 1), 0)
        

if __name__ == '__main__':
    unittest.main()
