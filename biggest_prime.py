#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 01:45:27 2025

@author: LiamBiam
"""

import numpy as np

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisors = np.arange(3, int(np.sqrt(n)) + 1, 2)
    return not np.any(n % divisors == 0)

# print(is_prime(2068))
# print(is_prime(2069))

biggest_prime = 3
number_range = 10**4
for n in range(number_range - 1, 1, -1):
    if is_prime(n):
        biggest_prime = n
        break
        
print(n)
    