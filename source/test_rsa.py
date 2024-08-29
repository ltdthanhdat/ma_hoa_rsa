# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import unittest
from rsa import RSA
class TestRSA(unittest.TestCase):
    def test_RSA_small_numbers(self):
        p = 61
        q = 53
        message = 65
        encrypted_message, decrypted_message = RSA(p, q, message)
        self.assertEqual(decrypted_message, message)
        self.assertNotEqual(encrypted_message, message)
    
    def test_RSA_large_numbers(self):
        p = 38104853
        q = 48784507
        message = 12
        encrypted_message, decrypted_message = RSA(p, q, message)
        self.assertEqual(decrypted_message, message)
        self.assertNotEqual(encrypted_message, message)

if __name__ == '__main__':
    unittest.main()
