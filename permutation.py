#!/usr/bin/python
# -*- coding: utf-8 -*-

def permutations(iterable, k, l):
    if k == l - 1:
        print iterable
    else:
        for i in range(k, l):
            iterable[k], iterable[i] = iterable[i], iterable[k]
            permutations(iterable, k+1, l)
            iterable[k], iterable[i] = iterable[i], iterable[k]
    
a = [1,2,3]
permutations(a, 0, len(a))
    
