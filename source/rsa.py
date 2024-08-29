# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

from math import gcd
from modular_calculation import modular_exponentiation, modular_multiplication
from generate_prime_number import generate_prime_number_greater_than
def RSA(p: int, q: int, message: int):
    n = p * q
    t = (p - 1) * (q - 1)
    # public key
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    # private key
    j = 0
    while True:
        if modular_multiplication(j, e, t) == 1:
            d = j
            break
        j += 1

    print(f"Public key is ({e}, {n})")
    print(f"Private key is ({d}, {n})")
    # encryption
    e_mes = modular_exponentiation(message, e, n)
    print(f"Encrypted message is {e_mes}")

    # decryption
    d_mes = modular_exponentiation(e_mes, d, n)
    print(f"Decrypted message is {d_mes}")

# Testcase - 1
print('case 1')
RSA(generate_prime_number_greater_than(1500), generate_prime_number_greater_than(1000), message=12)
print('-----------------------')
# Testcase - 2
print('case 2')
RSA(generate_prime_number_greater_than(10), generate_prime_number_greater_than(14), message=12)
