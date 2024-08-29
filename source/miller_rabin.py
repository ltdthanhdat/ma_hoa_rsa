# Name: Lê Thành Đạt
# Student ID: 20216811
# Class: 150328
# Project: 3 - Xây dựng chương trình sinh số nguyên tố (lớn hơn N cho trước) và mã hóa RSA
# Date: 20/6/2024

import random
def miller_rabin(n, k):
    # n: số nguyên tố cần kiểm tra
    # k: số bước lặp
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True