# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

from random import randint
from miller_rabin import miller_rabin

def generate_candidate_number_greater_than(n):
    while True:
        candidate = randint(n + 1, n + 101)
        if  candidate % 2 == 1 or candidate == 2:
            return candidate
def generate_prime_number_greater_than(n):
    p = 4
    while not miller_rabin(p, 40):
        p = generate_candidate_number_greater_than(n)
    return p