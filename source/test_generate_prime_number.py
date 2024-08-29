# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import unittest
from miller_rabin import miller_rabin
from generate_prime_number import  generate_prime_number_greater_than

class TestRandomNumberGeneration(unittest.TestCase):
    def test_generate_prime_number_greater_than(self):
        n = 10
        for _ in range(10):
            result = generate_prime_number_greater_than(n)
            self.assertTrue(result > n)
            self.assertTrue(miller_rabin(result, 40))

if __name__ == '__main__':
    unittest.main()
