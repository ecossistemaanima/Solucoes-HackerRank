#!/bin/python3

"""Abordagem de Dois Ponteiros (Two Pointer Algorithm)."""

def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    l, r = 0, len(s) - 1

    while l < r: # (Enquanto o ponteiro de l for menor que r)
        if s[l] != s[r]:
            if is_palindrome(s[l+1:r+1]):
                return l
            if is_palindrome(s[l:r]):
                return r
            return -1
        l += 1
        r -= 1
    return -1

if __name__ == '__main__':
    print(palindromeIndex('baab'))