# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import unittest
from miller_rabin import miller_rabin
class TestMillerRabin(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(miller_rabin(2, 40))
        self.assertTrue(miller_rabin(3, 40))
        self.assertTrue(miller_rabin(5, 40))
        self.assertTrue(miller_rabin(11, 40))
        self.assertTrue(miller_rabin(1000000007, 40))

    def test_non_prime_numbers(self):
        self.assertFalse(miller_rabin(1, 40))
        self.assertFalse(miller_rabin(4, 40))
        self.assertFalse(miller_rabin(100, 40))
        self.assertFalse(miller_rabin(1000000008, 40))

if __name__ == '__main__':
    unittest.main()