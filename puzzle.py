#!/usr/bin/python
# -*- coding: utf-8 -*-

# Solve problems like: "ODD + ODD = EVEN"

import re
import string
import itertools
from timing import *

@timing
def solve(formula):
    """
    solve the formula
    Eg. formula is a string like "ODD + ODD = EVEN"
    return the possible answers to the formula 
    """
    for i in fill_in(formula):
        if valid(i):
            return i

def fill_in(formula):
    """
    fill all possible numeric permutation to the formula
    Eg. To "ODD + ODD = EVEN"
    possible permutations are:
    "122 + 122 = 3435"
    "133 + 133 = 4245"
    ...
    return all the possible permutations  
    """
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    numbers = '0123456789'
    for seq in itertools.permutations(numbers, len(letters)):
        table = string.maketrans(letters, ''.join(seq))
        yield string.translate(formula, table)

def valid(string):
    try:
        if not re.findall(r'\b0[0-9]+', string) and eval(string) is True:
            return True
    except:
        return False


formula = "TWO + TWO == FOUR"
for _ in range(10):
    print solve(formula)
