
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Some scripts that can tell the max subpalindorme in a string.
#from timing import *

#@timing
import time

def subpalindrome_naive(string):
    max_len = -1
    result = ()
    count = 0
    for i in range(len(string)):
        for n in range(i, len(string)):
            palin, temp = palindrome(string[i:n+1])
            count += temp + 1
            if palin and n - i > max_len:
               result = (i, n)
               max_len = n - i
#    print count
    return result
               
def subpalindrome(string):
    max_len, result = -1, ()
    count = 0
    string = string.lower()
    for i in range(len(string)):
        start, end, temp = max_expand(string, i)
        count += temp
        if end - start > max_len:
            max_len = end - start
            result = (start, end)
 #   print count
    return result

def max_expand(string, n):
    s1, e1 = search_even(string, n)
    s2, e2 = search_odd(string, n)
    if abs(e1 - s1) >= abs(e2 - s2):
        return s1, e1, max(e1 + e2 - 2 * n, 2)
    else:
        return s2, e2, max(e2 + e1 - 2 * n, 2)


def search_even(string, n):
    right = n + 1
    length = len(string)
    while n >= 0 and right < length and string[n] == string[right]:
        n -= 1
        right += 1
    if right == n + 1:
        return n, n
    else:
        return n+1, right-1

def search_odd(string, n):
    left = right = n
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return left+1, right-1
    

def palindrome(string):
    """
    return if the string is a palindrome
    Eg. "Racecar" -> True
        "abbs"    -> False
    """
    string = string.lower()
    return string == string[::-1], len(string)
def test():
#    assert palindrome("Racecar") == True
#    assert palindrome("abbs") == False
#    assert palindrome("aAB") == False
#    assert palindrome("Aa") == True
#    assert palindrome("a") == True
#    assert palindrome("") == True
    assert subpalindrome_naive("RacecarX") == (0, 6)
    assert subpalindrome_naive("aaaaaa") == (0, 5)
    assert subpalindrome_naive("a") == (0, 0)
    assert subpalindrome_naive("aaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaa") == (0, 69)
   
    assert subpalindrome("RacecarX") == (0, 6)
    assert subpalindrome("aaaaaa") == (0, 5)
    assert subpalindrome("a") == (0, 0)
    assert subpalindrome("aaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaa") == (0, 69)
    print "test pass"

test()

def timing(n, func, *args, **kwargs):
    time1 = time.clock()
    for _ in range(n):
        func(*args, **kwargs)
    print "%6.4f seconds" % (time.clock() - time1)
        
timing(1000, subpalindrome_naive, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
timing(1000, subpalindrome, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print len("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


